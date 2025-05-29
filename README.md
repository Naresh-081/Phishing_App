# AI ANTI Phishing_App

# 🔎 Phishing Detection Dashboard

A web application that detects phishing URLs and emails using machine learning models and Google Safe Browsing API.

## Features

- **URL Phishing Detection** - Custom BERT model + Google Safe Browsing API validation
- **Email Phishing Detection** - Machine learning classification of suspicious emails  
- **Real-time Results** - Instant analysis with color-coded feedback
- **Clean Web Interface** - Easy-to-use dashboard

## Installation

1. **Clone and setup**
   ```bash
   git clone <your-repo-url>
   cd phishing-detection-dashboard
   pip install -r requirements.txt
   ```

2. **Configure API key**
   ```bash
   # Create .env file
   echo "GOOGLE_API_KEY=your_api_key_here" > .env
   ```

3. **Run the app**
   ```bash
   uvicorn main:app --reload
   ```

Visit `http://localhost:8000` to access the dashboard.

## How It Works

**URL Analysis**: Submit a URL to get predictions from both a trained BERT model and Google's threat database.

**Email Analysis**: Paste email content to detect phishing attempts using machine learning.

## Tech Stack

- **Backend**: FastAPI, Python
- **ML Models**: BERT (URLs), Custom classifier (Emails)
- **Frontend**: HTML/CSS with Jinja2
- **API**: Google Safe Browsing

## Project Structure

```
├── main.py                          # FastAPI application
├── templates/index.html             # Web interface
├── bert_urlmodel/bertmodel.py       # URL detection model
├── email_model/model/emailmodel.py  # Email detection model
├── requirements.txt                 # Dependencies
└── .env                            # Environment variables
```

## Requirements

- Python 3.7+
- Google Safe Browsing API key
- Required packages: `fastapi`, `uvicorn`, `transformers`, `requests`, `jinja2`