# 🤖 Assistant Bot

## 🧠 Project Description

Assistant Bot is a Telegram-based productivity assistant designed to streamline team communication and task tracking. It offers quick access to weekly reports, task lists, and provides an interface for users to ask questions. Built with Python and the `python-telegram-bot` library, this bot simplifies team operations within Telegram, providing a menu-driven interface for intuitive interaction.

# 🗺️ Project Map (Structure)
~~~bash
assistant-bot/
├── bot.py                    # Main application logic
├── README.md                 # Project description and setup guide
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (e.g. bot token)
├── utils/                    # Helper functions (e.g. keyboards, messages)
│   └── menu.py               # Main menu UI
├── handlers/                 # Bot handlers
│   ├── start.py              # /start command handler
│   ├── callback.py           # Inline button callback logic
│   └── messages.py           # Text message handler
└── LICENSE
~~~

## ✨ Features

- 📊 Weekly Report Overview
- 📋 Task List Display
- ❓ Q&A Prompting
- 🧠 Smart reply for common phrases (e.g., "tasks", "review reports")
- 🧵 InlineKeyboard navigation

  ### Prerequisites

- Python 3.10+
- Telegram account
- Telegram bot token (from [@BotFather](https://t.me/BotFather))

  ## Clone the repo:

```bash
git clone https://github.com/yourusername/Assistant_Bot.git
cd Assistant_Bot
~~~
