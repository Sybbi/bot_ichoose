#data_handler.py
import os
from datetime import datetime


def save_entry(section: str, text: str):
    os.makedirs("data", exist_ok=True)
    filename = os.path.join("data", f"{section}.txt")

    with open(filename, "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        file.write(f"[{timestamp}] {text}\n")

def read_entries(section: str) -> str:
    """
    Читает все записи из соответствующего файла раздела и возвращает как одну строку.
    Если файл пуст или не существует — сообщает об этом.
    """
    filename = os.path.join("data", f"{section}.txt")

    if not os.path.exists(filename):
        return "Записей пока нет."  # Если файла нет — возвращаем сообщение

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read().strip()  # Удаляем пробелы и перевод строки по краям
        return content if content else "Записей пока нет."  # Если файл пуст — сообщаем