import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_ai(prompt_text):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # ✅ BEST CHOICE
            messages=[
                {"role": "user", "content": prompt_text}
            ],
            temperature=0.7
        )

        return {
            "status": "success",
            "data": response.choices[0].message.content
        }

    except Exception as e:
        error_msg = str(e)

        if "429" in error_msg or "rate" in error_msg.lower():
            return {
                "status": "retry",
                "message": "⚠️ Too many requests. Please wait a few seconds and try again."
            }

        return {
            "status": "error",
            "message": error_msg
        }