from telegram import Update
from telegram.ext import ContextTypes
from keyboards.main_menu import get_main_menu

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello! I'm a helper bot. Choose an action:",
        reply_markup=get_main_menu()
    )
