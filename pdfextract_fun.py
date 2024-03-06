import warnings
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
# Filter warnings about inputs not requiring gradients
warnings.filterwarnings("ignore", message="None of the inputs have requires_grad=True. Gradients will be None")
warnings.filterwarnings("ignore", message="torch.meshgrid: in an upcoming release, it will be required to pass the indexing argument.")

import cv2
import os
import fitz  # PyMuPDF
import numpy as np
import re
import pytesseract
from PIL import Image
from tqdm import tqdm 
import torch
from unilm.dit.object_detection.ditod import add_vit_config

from detectron2.config import CfgNode as CN
from detectron2.config import get_cfg
from detectron2.utils.visualizer import ColorMode, Visualizer
from detectron2.data import MetadataCatalog
from detectron2.engine import DefaultPredictor


# Step 1: instantiate config
cfg = get_cfg()
add_vit_config(cfg)
cfg.merge_from_file("cascade_dit_base.yml")

# Step 2: add model weights URL to config
cfg.MODEL.WEIGHTS = "publaynet_dit-b_cascade.pth"

# Step 3: set device
cfg.MODEL.DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Step 4: define model
predictor = DefaultPredictor(cfg)

def analyze_image(img):
    
    md = MetadataCatalog.get(cfg.DATASETS.TEST[0])
    if cfg.DATASETS.TEST[0]=='icdar2019_test':
        md.set(thing_classes=["table"])
    else:
        md.set(thing_classes=["text","title","list","table","figure"])
    
    output = predictor(img)["instances"]
    v = Visualizer(img[:, :, ::-1],
                    md,
                    scale=1.0,
                    instance_mode=ColorMode.SEGMENTATION)
    result = v.draw_instance_predictions(output.to("cpu"))
    result_image = result.get_image()[:, :, ::-1]
    
    return result_image, output, v



def convert_pdf_to_jpg(pdf_path, output_folder, zoom_factor=2):
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)

        # Adjust zoom factor for higher resolution
        mat = fitz.Matrix(zoom_factor, zoom_factor)  # Create a Matrix with the zoom factor
        pix = page.get_pixmap(matrix=mat)  # Render the page using the matrix

        output_file = f"{output_folder}/page_{page_num}.jpg"
        pix.save(output_file)



def process_jpeg_images(output_folder):
     for page_num in tqdm(range(len(os.listdir(output_folder))), desc="Processing the pdf"):
         file_path = f"{output_folder}/page_{page_num}.jpg"
         img = cv2.imread(file_path)
         if img is None:
             print(f"Failed to read {file_path}. Skipping.")
             continue
         result_image, output, v = analyze_image(img)

         # Saving logic
         save_extracted_instances(img, output, page_num,output_folder)



def save_extracted_instances(img, output, page_num, dest_folder, confidence_threshold=0.8):
    class_names = {
        0: "text",
        1: "title",
        2: "list",
        3: "table",
        4: "figure"
    }

    threshold_value = 0  # Standard deviation threshold
    min_height = 0  # Minimum height threshold

    instances = output.to("cpu")
    boxes = instances.pred_boxes.tensor.numpy()
    class_ids = instances.pred_classes.tolist()
    scores = instances.scores.tolist()  # Get prediction scores

    image_counter = 1
    for box, class_id, score in zip(boxes, class_ids, scores):
        # Check if the prediction score meets the confidence threshold
        if score >= confidence_threshold:
            class_name = class_names.get(class_id, "unknown")

            # Save only if class is 'figure' or 'table'
            if class_name in ["figure", "table","text"]:
                x1, y1, x2, y2 = map(int, box)
                cropped_image = img[y1:y2, x1:x2]

                if np.std(cropped_image) > threshold_value and (y2 - y1) > min_height:
                    save_path = os.path.join(dest_folder, f"page_{page_num}_{class_name}_{image_counter}.jpg")
                    cv2.imwrite(save_path, cropped_image)
                    image_counter += 1


def delete_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)



def rename_files_sequentially(folder_path):
    # Regex pattern to match 'page_{page_num}_{class_name}_{image_counter}.jpg'
    pattern = re.compile(r'page_(\d+)_(\w+)_(\d+).jpg', re.IGNORECASE)

    # List files in the folder
    files = os.listdir(folder_path)

    # Filter and sort files based on the regex pattern
    sorted_files = sorted(
        [f for f in files if pattern.match(f)],
        key=lambda x: (int(pattern.match(x).group(1)), pattern.match(x).group(2).lower(), int(pattern.match(x).group(3)))
    )

    # Initialize an empty dictionary for counters
    counters = {}

    for filename in sorted_files:
        match = pattern.match(filename)
        if match:
            page_num, class_name, _ = match.groups()
            class_name = class_name.lower()  # Convert class name to lowercase

            # Initialize counter for this class if it doesn't exist
            if class_name not in counters:
                counters[class_name] = 1

            # New filename format: '{class_name}_{sequential_number}.jpg'
            new_filename = f"{class_name}_{counters[class_name]}.jpg"
            counters[class_name] += 1

            # Rename the file
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

            #print(f"Renamed '{filename}' to '{new_filename}'")


def ocr_folder(folder_path):
    # Regex pattern to match 'text_{number}.jpg'
    pattern = re.compile(r'text_\d+\.jpg', re.IGNORECASE)

    # Create a subfolder for the OCR text files
    ocr_text_folder = os.path.join(folder_path, "ocr_results")
    if not os.path.exists(ocr_text_folder):
        os.makedirs(ocr_text_folder)

    for filename in os.listdir(folder_path):
        if pattern.match(filename):
            image_path = os.path.join(folder_path, filename)
            text = ocr_image(image_path)
            
            # Save the OCR result to a text file in the subfolder
            text_file_name = filename.replace('.jpg', '.txt')
            text_file_path = os.path.join(ocr_text_folder, text_file_name)
            with open(text_file_path, 'w') as file:
                file.write(text)
            
            #print(f"OCR result for {filename} saved to {text_file_path}\n")

def ocr_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text