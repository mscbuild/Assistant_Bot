from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters

# Main menu
def get_main_menu():
    keyboard = [
        [InlineKeyboardButton("📊 Report", callback_data='report')],
        [InlineKeyboardButton("❓ Question", callback_data='question')],
        [InlineKeyboardButton("📋 Task list", callback_data='tasks')],
    ]
    return InlineKeyboardMarkup(keyboard)

# Team /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello! I'm a helper bot. Choose an action:", 
        reply_markup=get_main_menu()
    )

# Processing menu buttons
async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'report':
        await query.edit_message_text("📈 Weekly report:\n\n🗓 Week: July 7– July 13\n✅ Tasks completed:12\n❗ Expired: 2\n📌 New tasks: 5")

    elif query.data == 'question':
        await query.edit_message_text("❓ Write me your question and I will try to help!")

    elif query.data == 'tasks':
        tasks = [
            "✅ Complete the presentation",
            "🕐 Schedule a meeting",
            "❗ Write a project report",
            "📞 Call the client"
        ]
        task_list = "\n".join(tasks)
        await query.edit_message_text(f"📋 Current tasks:\n\n{task_list}")

# Reply to text messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.lower()

    if "привет" in msg:
        await update.message.reply_text("👋 Hello! How can I help you?")
    elif "отчёт" in msg:
        await update.message.reply_text("📊 Your latest report is available via the 'Report' button in the menu.")
    else:
        await update.message.reply_text("🤔I don't understand this message yet. Use the menu!")

# Launching the application
app = ApplicationBuilder().token("your token").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(menu_callback))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("✅ The bot has been launched...")
app.run_polling()
