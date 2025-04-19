#bot.py

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

from config import API_KEY
from data_handler import save_entry
from utils import get_main_menu


# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = get_main_menu()
    await update.message.reply_text("Привет! Выбери раздел:", reply_markup=keyboard)


# Обработка нажатий кнопок
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    context.user_data["section"] = query.data
    await query.edit_message_text(f"Ты выбрал раздел: {query.data}. Напиши, что хочешь туда записать.")


# Обработка текстовых сообщений
async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    section = context.user_data.get("section")
    if not section:
        await update.message.reply_text("Сначала выбери раздел командой /start.")
        return

    text = update.message.text
    save_entry(section, text)
    await update.message.reply_text(f"Записал в раздел '{section}': {text}")


def main():
    app = ApplicationBuilder().token(API_KEY).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))

    print("Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()
