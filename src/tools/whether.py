from langchain.tools import tool
import requests
import os
from dotenv import load_dotenv
YOUR_ACCESS_KEY = "116ba3b03dc58aba85fc5a30ea99c0c1"

@tool
def weather_API(city:str):
  '''this is tool used to get information about the temperatures and rain probability'''
  url = f"http://api.weatherstack.com/forecast?access_key={YOUR_ACCESS_KEY}&query={city}"
  response = requests.get(url)
  data = response.json()
  if "error" in data:
    return {"error": data["error"]["info"]}

  return {
        "city": city,
        "temperature": data["current"]["temperature"],
        "rainfall_mm": data["current"]["precip"]
    }


print(weather_API.invoke({"city": "hyderabad"}))
    