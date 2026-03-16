from elevenlabs import generate,play,set_api_key
def text_to_speech(text):
  set_api_key("your_key")
  audio = generate(
    text=text,
    voice="rachel"
  )
  return audio

text = "Hello, this is a test message."
output = text_to_speech(text)
play(output)