from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

app = FastAPI()

model = genai.GenerativeModel("gemini-1.5-flash")


class TextRequest(BaseModel):
    text: str


@app.get("/")
def home():
    return {"message": "LinguaType AI Backend is running"}


@app.post("/correct")
def correct_text(request: TextRequest):
    prompt = f"Correct the grammar and spelling of this sentence. Return only corrected sentence: {request.text}"
    response = model.generate_content(prompt)
    return {"result": response.text.strip()}


@app.post("/translate-kannada")
def translate_kannada(request: TextRequest):
    prompt = f"Translate this text to Kannada. Return only translation: {request.text}"
    response = model.generate_content(prompt)
    return {"result": response.text.strip()}


@app.post("/professional")
def professional_text(request: TextRequest):
    prompt = f"Rewrite this sentence professionally. Return only rewritten sentence: {request.text}"
    response = model.generate_content(prompt)
    return {"result": response.text.strip()}


@app.post("/explain")
def explain_text(request: TextRequest):
    prompt = f"Explain the grammar mistake in this sentence in simple words: {request.text}"
    response = model.generate_content(prompt)
    return {"result": response.text.strip()}