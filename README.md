# 🤖 Assistant Bot
 ![](https://komarev.com/ghpvc/?username=mscbuild) 
 ![](https://img.shields.io/github/license/mscbuild/Assistant_Bot) 
 ![](https://img.shields.io/badge/PRs-Welcome-green)
![](https://img.shields.io/badge/code%20style-python-green)
![](https://img.shields.io/github/stars/mscbuild)
![](https://img.shields.io/badge/Topic-Github-lighred)
![](https://img.shields.io/website?url=https%3A%2F%2Fgithub.com%2Fmscbuild)


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

  ## 1.Clone the repo:

~~~bash
git clone https://github.com/yourusername/Assistant_Bot.git
cd Assistant_Bot
~~~

## 2.Create a virtual environment and activate it:
~~~bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
~~~

## 3. Install dependencies:
~~~bash
pip install -r requirements.txt
~~~

## 4. Set your bot token in .env:
~~~bash
BOT_TOKEN=your_token_here
~~~

## 5. Run the bot:
~~~bash
python bot.py
~~~

# 🧱 Tech Stack

- Python 3.10+

- python-telegram-bot

- dotenv (for managing environment variables)

# 📋 Checklist

 - ✅ Start command handler

 - ✅ Inline keyboard main menu

 - ✅ Report display

 - ✅ Task list generation

 - ✅ Question prompt handling

 - ✅ Basic natural language message recognition

 - ☐ Logging integration

 - ☐ Persistent storage for tasks/reports

 - ☐ Unit testsStart

   # 📦  What is needed for deployment

| File                        | Purpose                                            |
| --------------------------- | -------------------------------------------------- |
| `Dockerfile`                | Building a container for local/cloud running       |
| `Procfile`                  | To start Heroku worker                             |
| `.env`                      | Local environment variables                        |
| `requirements.txt`          | Installing dependencies                            |
| `bot.py` and other modules  | Bot's main code                                    |


# 📄 License

> MIT License
 

 
