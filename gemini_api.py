import os
from dotenv import load_dotenv
import requests
# Load environment variables from .env file (if available)
load_dotenv()
#export GEMINI_API_KEY="AIzaSyDGBfmHiDyQGMVKQt9Fn2bXuEq0eL5ITjg"
# Get API key from environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# Google Gemini API Endpoint
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

def get_gemini_response(prompt):
    """Sends a prompt to the Gemini API and returns the AI response."""
    
    if not prompt:
        return "Error: Prompt cannot be empty."

    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        response.raise_for_status()  # Raise error for HTTP errors

        data = response.json()
        return data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "No response")

    except requests.exceptions.RequestException as e:
        return f"API Error: {str(e)}"
