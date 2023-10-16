from dotenv import find_dotenv,load_dotenv
from transformers import pipeline
load_dotenv(find_dotenv())

#imagetotext

def img2text(url):
    image_to_text=pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")
    
    text=image_to_text(url)
    
    print(text)
    return text
img2text("AKL_0483.jpg")