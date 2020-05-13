import telebot
import random
from telebot.types import Message

BOT_TOKEN = 'BOT_TOKEN=1274265608:AAFWLFOLZKO6CkJuSrqEySu0lv46cuWwJBk'

bot = telebot.TeleBot(BOT_TOKEN)

smiles = [
    '👍',
    '🏻',
    '😱',
    '😅',
    '🙊',
    '😙',
    '🤓',
    '😞',
    '☹',
    '☺',
    '😋',
]


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Hello world')


@bot.message_handler(func=lambda message: True)
def upper(message: Message):
    bot.reply_to(message, random.choice)


bot.polling()

