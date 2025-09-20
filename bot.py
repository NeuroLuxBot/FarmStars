import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
# === Логирование (Railway будет видеть логи в разделе Logs) ===
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)
# === /start ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Приветствую!\n\n"
        "Если ты хочешь использовать бота, то необходимо подписаться на наши каналы 👇\n"
        "🔗 https://t.me/sherif_among\n"
        "🔗 https://t.me/DezardyChannelTG"
    )
def main():
    token = os.getenv("BOT_TOKEN")  # Railway возьмет переменную отсюда
    if not token:
        logger.error("❌ BOT_TOKEN не найден! Проверь переменные окружения Railway.")
        return
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    logger.info("✅ Бот запущен и слушает обновления...")
    app.run_polling()
if __name__ == "__main__":
    main()
