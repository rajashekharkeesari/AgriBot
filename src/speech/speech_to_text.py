import whisper
model = whisper.load_model("base")
def speech_to_text():
  output = model.transcribe('voice.mp3')#whatsapp supports ogg
  return output['text']
output = speech_to_text()
