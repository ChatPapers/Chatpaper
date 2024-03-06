import gradio as gr
import os
import uuid  # Import the UUID library
from pdfextract_fun import *
from pdfsummary_fun import *
from imagesummary_fun import *
# Assuming all your defined functions are above and imported correctly into this script



def process_pdf(pdf_file,state):
    #base_name = os.path.splitext(os.path.basename(pdf_file.name))[0]
    unique_id = str(uuid.uuid4())  # Generate a unique identifier

    output_folder = os.path.join("processed_files", unique_id)  # Use UUID for the output folder name, within a parent directory
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Convert the uploaded PDF file to JPG images
    convert_pdf_to_jpg(pdf_file.name, output_folder)
    # Process the images to analyze and extract instances, then rename files sequentially and perform OCR
    process_jpeg_images(output_folder)
    #process_jpeg_images(output_folder)
    rename_files_sequentially(output_folder)
    ocr_folder(output_folder)
    image_files = [os.path.join(output_folder, f) for f in os.listdir(output_folder) 
                   if f.endswith('.jpg') and ('figure' in f or 'table' in f)]

    #images = [Image.open(f) for f in image_files]
    images = [(Image.open(f), os.path.basename(f).split('.')[0]) for f in image_files]

    # For demonstration, let's just return the path to the output folder
    # In a real app, you'd want to return images, texts, or links to download the results
    return images, output_folder

def call_pdf_summary(state):
    ocr_results_folder = os.path.join(state, "ocr_results")
    summary = pdf_summary(ocr_results_folder)  # Assuming pdf_summary accepts an output folder argument
    return summary


def handle_summary_button_click(selected_images):
    # Check if any image is selected
    summary = get_image_summary(selected_images)
    return summary

with gr.Blocks(theme=gr.themes.Monochrome()) as app:
    gr.Markdown("# ChatPaper!")
    state = gr.State()  # Initialize state
    
    with gr.Row():
        file_input = gr.File(type="filepath", label="Upload a PDF")
        
    with gr.Row():
        gallery_output = gr.Gallery(label="Extracted Figures and Tables", show_label=True,columns=[3], rows=[1], object_fit="contain", height="auto")
        with gr.Column():
            summary_output = gr.Textbox(label="PDF Summary")
            summary_button = gr.Button("Generate Summary")
    with gr.Row():
        # Initialize Dropdown without choices; they will be set dynamically
        image_input = gr.Image(label="Select an Figure or Table for analysis",type='filepath',show_label=True, height="auto")
        with gr.Column():
            image_summary_output = gr.Textbox(label="Figure or Table analysis")
            image_summary_button = gr.Button("Generate Figure or Table analysis")
            


    file_input.change(process_pdf, inputs=[file_input, state], outputs=[gallery_output,  state])
    summary_button.click(call_pdf_summary, inputs=[state], outputs=[summary_output])
    image_summary_button.click(handle_summary_button_click, inputs=image_input, outputs=image_summary_output)

    # Note: Authentication details removed for security reasons
app.launch()  # Launch the app with sharing enabled
