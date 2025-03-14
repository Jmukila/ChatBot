from flask import Flask, render_template, request
import os
from gemini_api import get_gemini_response  # Import function from gemini_api.py

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    
    if request.method == "POST":
        user_prompt = request.form.get("prompt")  # Get user input safely
        response_text = get_gemini_response(user_prompt)  # Call API function
    
    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(debug=True)
