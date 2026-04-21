from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL = "models/gemini-2.5-flash"


def generate_response(context, question):

    prompt = f"""
You are an AI assistant for AutoStream.

Use ONLY the provided context to answer the user's question.

Context:
{context}

Question:
{question}

Answer clearly and briefly.
"""

    try:
        resp = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )

        # Sometimes Gemini returns empty response
        if resp and hasattr(resp, "text") and resp.text:
            return resp.text.strip()

        return "I'm sorry, I couldn't generate a response."

    except Exception as e:
        print("LLM error:", e)
        return "Sorry, I'm having trouble accessing the AI service right now."
