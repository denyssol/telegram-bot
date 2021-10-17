import telebot

from app.config import settings

bot = telebot.TeleBot(settings.TOKEN)
print(bot.get_me())
