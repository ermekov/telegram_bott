import telebot
import webbrowser
from telebot import types
import sqlite3
import requests
import json

bot = telebot.TeleBot('7083395817:AAF7QjavKj8QHWdYoLiX6xUqpSmSsFTPD48')
API = "cced0bc6133666f728728356fda52d60"


@bot.message_handler(commands=['start','бастау','начать'])
def main(message):
    bot.send_message(message.chat.id, "Салем, жазғаныңа қуаныштымын! Қаланың атын жаз: ")

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message,f"Қазіргі уақытта ауа райы: {temp}")

        image = 'sunny.png' if temp < 5.0 else 'sun.png'
        file=open('./'+image,'rb')
        bot.send_photo(message.chat.id,file)
    else:
        bot.reply_to(message, "Қала атын дұрыс жазбадыңыз")


bot.polling(none_stop=True)