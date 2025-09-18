import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# === Логирование ===
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# === Команда /start ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_text(
            "👋 Приветствую!\n\n"
            "Если ты хочешь использовать бота, то необходимо подписаться на наши каналы 👇\n"
            "🔗 https://t.me/sherif_among\n"
            "🔗 https://t.me/DezardyChannelTG"
        )
    except Exception as e:
        logger.error(f"Ошибка в команде /start: {e}")

# === Запуск приложения ===
def main():
    TOKEN = os.getenv("BOT_TOKEN")
    if not TOKEN:
        logger.error("Не задана переменная окружения BOT_TOKEN")
        exit(1)

    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))

    logger.info("Бот запущен")
    application.run_polling()

if __name__ == "__main__":
    main()
