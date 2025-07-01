from telegram import Update
from telegram.ext import ContextTypes
from constants.data import REPORT, TASKS
from keyboards.main_menu import get_main_menu

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'report':
        await query.edit_message_text(REPORT)

    elif query.data == 'question':
        await query.edit_message_text("❓ Write me your question and I will try to help!")

    elif query.data == 'tasks':
        await query.edit_message_text(f"📋 Current tasks:\n\n{TASKS}")

    else:
        await query.edit_message_text("❗ Unknown command.")
