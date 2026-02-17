import random

responses = {
    "happy": [
        "That sounds wonderful! What made your day good?",
        "I am glad you are feeling happy!"
    ],
    "sad": [
        "I am here with you. Want to talk about it?",
        "That sounds difficult. You are not alone."
    ],
    "stress": [
        "That sounds overwhelming. Want to break it into smaller steps?",
        "Stress can be tough. Maybe a short break could help."
    ],
    "neutral": [
        "How has your day been so far?",
        "Would you like to share something interesting?"
    ]
}

def get_response(emotion):
    return random.choice(responses[emotion])
