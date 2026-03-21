from fastapi import FastAPI, Request
import requests
import tempfile
import os
import traceback
from dotenv import load_dotenv
import tensorflow as tf
from src.speech.speech_to_text import speech_to_text
from src.vision import load_model
from src.llm import agent
import numpy as np
from keras.utils import load_img, img_to_array
from dotenv import load_dotenv
print(tf.__version__)

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\ffmpeg-8.1-essentials_build\bin"
app = FastAPI()
model = load_model()


def predict_image(img_path, model):
    img = load_img(img_path, target_size=(224, 224))  
    img_array = img_to_array(img)                     

    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    predictions = model.predict(img_array)

    predicted_class = np.argmax(predictions, axis=1)[0]

    return f"Predicted class: {predicted_class}"
VERIFY_TOKEN = "EAAWcquZBxRgoBQZBBZBZAjJU2RD3UoVFEVqPMKLFUWWjha9by213vpjgucNSOKPHk8pZAeTPHiAeohlDmhXCNCOTB2i0W7pa1dr0zt0Npv9ZAcN87w5ZAiOMD6LZCDabVeihgC67oDLbMQZAs7rZCDJx8aqxl7Ll3Yiw85ZBiZAwvcZCogIlZBNPZAZChfqOyf9qtWI4eHpbkPRFPZAZAZAR9iiEXYjdmsw0XLJTe93dfe8ML4JW7gzGdKGmzE8ZAX5PPDUYwf9AN48TUXeVaIOCzQ7OaCZCua1A3QAZDZD"
WHATSAPP_TOKEN = "EAAWcquZBxRgoBQ34Sxb4AqiB4nFGv0rsi0txl0bOY9iFNwsKr3bBaZBcBfSeEFRCSS9GyjAeopUHara3cSiZCHnAFnC4MOZBLvQdVq8iIecihFwJAZByi5vPcZBx0qkrP4jmUtpo2aHm8TdL7reQP0uZBhyiiD45OypS3Niz0phUvJt1mhSHbe7so9ZCGvVDnxcqOvIl9dc3fXiZC3ZBTl9p7XVKzwXwNBBZCARlGIk3hbbOjq6sUQnAy4InUrV4ZBdNh3sKkPFO8EegykZBwFX6L7uztUXAZD"
PHONE_NUMBER_ID = 1081666781685980
  

from fastapi.responses import PlainTextResponse

@app.get("/webhook")
async def verify_webhook(request: Request):
    params = request.query_params

    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

 
    print("MODE:", mode)
    print("TOKEN FROM META:", token)
    print("YOUR VERIFY_TOKEN:", VERIFY_TOKEN)
    print("CHALLENGE:", challenge)

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return PlainTextResponse(content=str(challenge))

    return PlainTextResponse(content="Verification failed", status_code=403)


@app.post("/webhook")
async def receive_message(request: Request):
    data = await request.json()

    try:
        entry = data["entry"][0]
        changes = entry["changes"][0]
        value = changes["value"]

        messages = value.get("messages")

        if not messages:
            return {"status": "no message"}

        message = messages[0]
        from_number = message["from"]

        text = None

       
        if message["type"] == "text":
            text = message["text"]["body"]
            print(text)

       
        elif message["type"] == "audio":
            media_id = message["audio"]["id"]
            audio_path = download_media(media_id, "ogg")
            text = speech_to_text(audio_path)

        
        elif message["type"] == "image":
            media_id = message["image"]["id"]
            image_path = download_media(media_id, "jpg")

            image_description = predict_image(image_path,model)

            text = image_description

    
        if text:
            response = agent.run(text)

            if hasattr(response, "content"):
                reply_text = response.content
            else:
                reply_text = str(response)

            send_whatsapp_message(from_number, reply_text)

    except Exception as e:
        print("Error:", e)
        traceback.print_exc()

    return {"status": "ok"}



def download_media(media_id, ext):
    url = f"https://graph.facebook.com/v19.0/{media_id}"

    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}"
    }

   
    res = requests.get(url, headers=headers)
    print("MEDIA RESPONSE:", res.json())
    data = res.json()
    if "url" not in data:
        raise Exception(f"Failed to get media URL: {data}")
    media_url = data["url"]
    media_res = requests.get(media_url, headers=headers)

    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{ext}") as tmp:
        tmp.write(media_res.content)
        return tmp.name



def send_whatsapp_message(to, message):
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {
            "body": str(message)
        }
    }

    requests.post(url, headers=headers, json=payload)