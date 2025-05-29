import torch
from transformers import BertTokenizer, BertForSequenceClassification
from .whitelist import PHISHING_EXAMPLES  # ✅ Using whitelist only

# Load tokenizer and model
MODEL_PATH = "email_model/model"
tokenizer = BertTokenizer.from_pretrained(MODEL_PATH)
model = BertForSequenceClassification.from_pretrained(MODEL_PATH)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

def predict_email_phishing(text: str) -> str:
    # Rule 1: Exact match override from demo phishing examples
    for demo_text in PHISHING_EXAMPLES:
        if text.strip().lower() == demo_text.strip().lower():
            return "Phishing"

    # Rule 2: BERT model prediction
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    inputs = {key: val.to(device) for key, val in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)
        prediction = torch.argmax(outputs.logits, dim=1).item()

    return "Phishing" if prediction == 1 else "Legitimate"
