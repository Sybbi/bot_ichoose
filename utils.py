#utils.py

from telegram import InlineKeyboardMarkup, InlineKeyboardButton


def get_main_menu():
    keyboard = [
        [
            InlineKeyboardButton("🧠 Важные вещи", callback_data="важные_вещи"),
            InlineKeyboardButton("💬 Промты", callback_data="промты"),
        ],
        [
            InlineKeyboardButton("❤️ Женщины", callback_data="женщины"),
            InlineKeyboardButton("📁 Другое", callback_data="другое"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
