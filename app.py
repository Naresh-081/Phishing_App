import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import requests

# Custom Model Imports
from bert_urlmodel.bertmodel import predict_url
from email_model.model.emailmodel import predict_email_phishing

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# App Setup
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Route for Home Page
@app.get("/", response_class=HTMLResponse)
def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# URL Phishing Detection Handler
@app.post("/check_url", response_class=HTMLResponse)
def handle_url_form(request: Request, url: str = Form(...)):
    # BERT model prediction
    bert_prediction = predict_url(url)

    # Google Safe Browsing API prediction
    api_url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={API_KEY}"
    payload = {
        "client": {"clientId": "phishing-detector", "clientVersion": "1.0"},
        "threatInfo": {
            "threatTypes": [
                "MALWARE", "SOCIAL_ENGINEERING",
                "UNWANTED_SOFTWARE", "POTENTIALLY_HARMFUL_APPLICATION"
            ],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }
    response = requests.post(api_url, json=payload)
    result = response.json()
    google_prediction = "Phishing" if result.get("matches") else "Legitimate"

    return templates.TemplateResponse("index.html", {
        "request": request,
        "url": url,
        "bert_result": bert_prediction,
        "google_result": google_prediction,
        "email_input": "",
        "email_prediction": ""
    })

# Email Phishing Detection Handler
@app.post("/check_email", response_class=HTMLResponse)
def handle_email_form(request: Request, email: str = Form(...)):
    email_result = predict_email_phishing(email)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "email_input": email,
        "email_prediction": email_result,
        "url": "",
        "bert_result": "",
        "google_result": ""
    })
