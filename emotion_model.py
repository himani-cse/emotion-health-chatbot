import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Simple training dataset
data = {
    "text": [
        "I am very happy today",
        "I feel sad and lonely",
        "I am stressed about exams",
        "I feel relaxed and calm",
        "I am worried about future",
        "I feel great and excited",
        "I am tired and depressed"
    ],
    "emotion": [
        "happy",
        "sad",
        "stress",
        "neutral",
        "stress",
        "happy",
        "sad"
    ]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])

model = LogisticRegression()
model.fit(X, df["emotion"])

def predict_emotion(text):
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)
    return prediction[0]
