from transformers import BertTokenizer, BertForSequenceClassification
import torch
import os

# Defining the path to saved model directory
MODEL_DIR = "bert_urlmodel/model/bert_phishing_model"



# Load tokenizer and model from the saved directory
tokenizer = BertTokenizer.from_pretrained(MODEL_DIR)
model = BertForSequenceClassification.from_pretrained(MODEL_DIR)
model.eval()

# Prediction function
def predict_url(url: str) -> str:
    # Tokenize the input URL
    inputs = tokenizer(url, return_tensors="pt", padding=True, truncation=True, max_length=512)

    # Make prediction
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()

    # Return label
    return "Phishing" if predicted_class == 1 else "Benign"
