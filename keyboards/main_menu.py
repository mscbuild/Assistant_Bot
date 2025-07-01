from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def get_main_menu():
    keyboard = [
        [InlineKeyboardButton("📊 Report", callback_data='report')],
        [InlineKeyboardButton("❓ Question", callback_data='question')],
        [InlineKeyboardButton("📋 Task list", callback_data='tasks')],
    ]
    return InlineKeyboardMarkup(keyboard)
