# bot.py

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,  # Импортируем MessageHandler
    ContextTypes,
    filters,
)

from config import API_KEY
from data_handler import save_entry, read_entries # 💡 добавили read_entries
from utils import get_main_menu  # Импортируем get_main_menu

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Эта функция отправляет сообщение с кнопкой 'Start'.
    Пользователь нажимает на кнопку для начала работы с ботом.
    """
    # Создаем клавиатуру с кнопкой 'Start'
    start_button = [
        [InlineKeyboardButton("Start", callback_data='start')]
    ]
    start_keyboard = InlineKeyboardMarkup(start_button)
    
    # Отправляем сообщение с кнопкой 'Start'
    await update.message.reply_text("Привет! Нажми 'Start' для начала.", reply_markup=start_keyboard)

# Обработка нажатий кнопок
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Обработчик нажатия кнопок на клавиатуре.
    Сохраняет выбранный раздел и просит пользователя записать текст в этот раздел.
    """
    query = update.callback_query
    await query.answer()

    if query.data == 'start':
        # Когда нажимается кнопка Start, показываем основное меню
        keyboard = get_main_menu()  # Получаем основное меню
        await query.edit_message_text("Выберите раздел:", reply_markup=keyboard)
    elif query.data == "back_to_menu":
        keyboard = get_main_menu()
        await query.edit_message_text("Вы вернулись в главное меню. Выберите раздел:", reply_markup=keyboard)
    else:
        context.user_data["section"] = query.data
        entries = read_entries(query.data)
        message = f"Ты выбрал раздел: {query.data}.\n\nВот что у тебя есть:\n{entries}\n\nНапиши, что хочешь туда записать."

        # 💡 Добавим кнопку "Назад в меню"
        back_button = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Назад в меню", callback_data="back_to_menu")]
        ])

        await query.edit_message_text(message, reply_markup=back_button)


# Обработка текстовых сообщений
async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    """
    Функция для обработки текстовых сообщений от пользователя.
    Сохраняет сообщение в выбранный раздел.
    """
    section = context.user_data.get("section")
    if not section:
        await update.message.reply_text("Сначала выбери раздел командой /start.")
        return

    text = update.message.text
    save_entry(section, text)
    await update.message.reply_text(f"Записал в раздел '{section}': {text}")

def main():
    app = ApplicationBuilder().token(API_KEY).build()

    # Добавляем обработчики
    app.add_handler(CommandHandler("start", start))  # Команда /start
    app.add_handler(CallbackQueryHandler(button_handler))  # Обработка кнопок
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))  # Обработка текста

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
