from telebot.async_telebot import AsyncTeleBot
import asyncio

bot = AsyncTeleBot("Your token bot")

@bot.message_handler(func=lambda message: True)
async def echo(message):
    await bot.send_message(message.chat.id, f"You wrote: {message.text}")

if __name__ == "__main__":
    print("✅ The bot has been launched")
    asyncio.run(bot.polling())
