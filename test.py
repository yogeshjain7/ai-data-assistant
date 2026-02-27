import google.generativeai as genai

genai.configure(api_key="AIzaSyD_VLBGkfWVAfqzUkVt0Do_GSKX6Y7ePyM")

for m in genai.list_models():
    print(m.name)
