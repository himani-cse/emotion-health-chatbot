from emotion_model import predict_emotion
from responses import get_response
from mood_tracker import save_mood, load_history
import matplotlib.pyplot as plt

def show_mood_chart():
    history = load_history()

    if history is None:
        print("No mood history yet.")
        return

    emotion_counts = history["emotion"].value_counts()

    emotion_counts.plot(kind="bar")
    plt.title("Mood History")
    plt.xlabel("Emotion")
    plt.ylabel("Frequency")
    plt.show()

print("🤖 Emotional Support Chatbot")
print("Type 'exit' to quit")
print("Type 'mood' to see mood chart\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    if user_input.lower() == "mood":
        show_mood_chart()
        continue

    emotion = predict_emotion(user_input)
    save_mood(emotion, user_input)

    response = get_response(emotion)
    print("Bot:", response)
