import requests
import os
from dotenv import load_dotenv
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

# Load API key
load_dotenv(dotenv_path="api_key.env")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# OpenRouter API config
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}
MODEL = "mistralai/mistral-7b-instruct"

# Load BLIP model + processor once
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# ✅ Real BLIP captioning
def generate_base_caption(image):
    image = image.convert('RGB')  # Ensure format is correct
    inputs = processor(image, return_tensors="pt")
    with torch.no_grad():
        out = blip_model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

# Stylize using OpenRouter API
def stylize_caption(caption, style):
    prompt = (
        f"Rewrite the following image caption in a {style} style. "
        f"Keep it short and concise — max 1 to 2 lines.\n\n\"{caption}\""
    )
    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        response = requests.post(OPENROUTER_API_URL, headers=HEADERS, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"⚠️ Error: {e}"
