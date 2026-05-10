from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai

api_key = "AIzaSyCLueyvaUZhYeSgHBAI56YSvC3yUY-DbI4"

genai.configure(api_key=api_key)

app = FastAPI()

model = genai.GenerativeModel("gemini-2.0-flash-lite")


class TextRequest(BaseModel):
    text: str


@app.get("/")
def home():
    return {
        "message": "LinguaType AI Backend is running"
    }


def ask_gemini(prompt: str):
    try:
        response = model.generate_content(prompt)

        return {
            "result": response.text.strip()
        }

    except Exception as e:
        return {
            "result": f"AI error: {str(e)}"
        }


@app.post("/correct")
def correct_text(request: TextRequest):

    prompt = f"""
Correct the grammar and spelling of this sentence.
Return only the corrected sentence.

Sentence:
{request.text}
"""

    return ask_gemini(prompt)


@app.post("/translate-kannada")
def translate_kannada(request: TextRequest):

    prompt = f"""
Translate this text to Kannada.
Return only the Kannada translation.

Text:
{request.text}
"""

    return ask_gemini(prompt)


@app.post("/professional")
def professional_text(request: TextRequest):

    prompt = f"""
Rewrite this sentence professionally.
Return only the rewritten sentence.

Sentence:
{request.text}
"""

    return ask_gemini(prompt)


@app.post("/explain")
def explain_text(request: TextRequest):

    prompt = f"""
Explain the grammar mistake in this sentence in simple words.
Keep the explanation short.

Sentence:
{request.text}
"""

    return ask_gemini(prompt)