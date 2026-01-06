# Detection of Phishing Websites

## 📌 Project Overview
This project is a **machine learning–based web application** that detects whether a given website URL is **phishing or legitimate**.  
It helps users identify malicious websites and avoid online fraud by analyzing URL-based features and applying a trained ML model.

---

## 🚀 Features
- Classifies URLs as **Phishing** or **Legitimate**
- Machine learning model trained on real-world phishing datasets
- Web interface for user-friendly URL input
- Fast prediction with high accuracy
- Simple and intuitive UI

---

## 🛠 Tech Stack
- **Programming Language:** Python  
- **Machine Learning:** Scikit-learn (Gradient Boosting Classifier)  
- **Web Framework:** Flask  
- **Frontend:** HTML, CSS  
- **Data Processing:** Pandas, NumPy  

---

## ⚙️ How It Works
1. User enters a website URL.
2. URL features are extracted (length, special characters, suspicious patterns, etc.).
3. The trained **Gradient Boosting Classifier** analyzes the features.
4. The model predicts whether the URL is **Phishing** or **Legitimate**.
5. Result is displayed on the web interface.

---

## 🧠 Machine Learning Details
- **Algorithm Used:** Gradient Boosting Classifier  
- **Feature Extraction:** URL-based lexical features  
- **Dataset:** Phishing and legitimate website URLs  
- **Model Evaluation:** Accuracy-based performance measurement  

---


## 📂 Project Structure

phishing-website-detection/
│
├── app.py                     # Main Flask application (routes & prediction logic)
├── config.py                  # App configuration settings
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
│
├── model/
│   ├── model.pkl              # Trained machine learning model
│   └── scaler.pkl             # Feature scaler (if used)
│
├── src/
│   ├── __init__.py
│   ├── feature_extraction.py  # URL feature extraction logic
│   ├── preprocess.py          # Data preprocessing utilities
│   └── predict.py             # Model loading & prediction functions
│
├── training/
│   ├── train_model.py         # Model training script
│   ├── evaluate_model.py      # Model evaluation & metrics
│   └── dataset.csv            # Training dataset
│
├── templates/
│   └── index.html             # Frontend HTML template
│
├── static/
│   ├── css/
│   │   └── style.css          # Application styling
│   └── js/
│       └── script.js           # Client-side validation (optional)
│
├── tests/
│   └── test_prediction.py     # Unit tests for prediction logic
│
└── screenshots/
    ├── home_page.png           # UI screenshots for README
    └── result_page.png


