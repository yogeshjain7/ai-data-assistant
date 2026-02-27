import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def ask_ai(prompt_text):
    model = genai.GenerativeModel("models/gemini-2.5-flash")

    response = model.generate_content(prompt_text)

    return response.text