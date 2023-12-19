import os
import google.generativeai as genai
import PIL.Image

img = PIL.Image.open('ArduinoStarterKit.webp')

from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY=os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-pro-vision')
response = model.generate_content(["Explain the different components seen in this image. Then come up with some ideas for beginner projects with only the parts available in the image.", img])
response.resolve()

print(response.text)