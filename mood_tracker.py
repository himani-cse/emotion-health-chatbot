import pandas as pd
from datetime import datetime
import os

FILE_NAME = "mood_history.csv"

def save_mood(emotion, message):
    new_data = {
        "date": [datetime.now()],
        "emotion": [emotion],
        "message": [message]
    }

    df_new = pd.DataFrame(new_data)

    if os.path.exists(FILE_NAME):
        df = pd.read_csv(FILE_NAME)
        df = pd.concat([df, df_new], ignore_index=True)
    else:
        df = df_new

    df.to_csv(FILE_NAME, index=False)

def load_history():
    if os.path.exists(FILE_NAME):
        return pd.read_csv(FILE_NAME)
    return None
