from telegram import Update
from telegram.ext import ContextTypes

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.lower()

    if "привет" in msg:
        await update.message.reply_text("👋 Hello! How can I help you?")
    elif "отчёт" in msg:
        await update.message.reply_text("📊 Your latest report is available via the 'Report' button in the menu.")
    else:
        await update.message.reply_text("🤔 I don't understand. Please use the menu.")
