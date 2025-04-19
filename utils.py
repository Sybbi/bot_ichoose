#utils.py

from telegram import InlineKeyboardMarkup, InlineKeyboardButton


def get_main_menu():
    keyboard = [
        [
            InlineKeyboardButton("🧠 Важные вещи", callback_data="важные_вещи"),
            InlineKeyboardButton("💬 Промты", callback_data="промты"),
        ],
        [
            InlineKeyboardButton("❤️ Самочувствие", callback_data="Самочувствие"),
            InlineKeyboardButton("📁 Другое", callback_data="другое"),
        ],
        [
            InlineKeyboardButton("❤️ ссылки", callback_data="ссылки"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
