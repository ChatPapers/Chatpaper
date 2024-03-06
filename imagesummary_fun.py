import base64
import requests
import os 

from dotenv import load_dotenv
load_dotenv()  # This loads the variables from .env
openai_api_key = os.getenv('openai_api_key')
#openai_api_key = os.getenv('openai_api_key')
# Mock function to simulate image encoding and API call
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    


# Function to get summary from OpenAI GPT-4 Vision API
def get_image_summary(image_path):
    # Encode the selected image
    base64_image = encode_image_to_base64(image_path)

    # OpenAI API URL and Key
    api_url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",  # Update this if the model name changes
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    },
                    {
                        "type": "text",
                        "text": "You have provide an explanation for this figure or table. Consider elements like panels, axis, data and labels and etc."
                    }
                ]
            }
        ],
        "max_tokens": 1000
    }

    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "Failed to get summary. Please try again."