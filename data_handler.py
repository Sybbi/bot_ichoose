#data_handler.py
import os
from datetime import datetime


def save_entry(section: str, text: str):
    os.makedirs("data", exist_ok=True)
    filename = os.path.join("data", f"{section}.txt")

    with open(filename, "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        file.write(f"[{timestamp}] {text}\n")
