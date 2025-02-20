import telebot
import webbrowser
from telebot import types
import sqlite3
import requests
import json
from currency_converter import CurrencyConverter

bot = telebot.TeleBot('7083395817:AAF7QjavKj8QHWdYoLiX6xUqpSmSsFTPD48')
API_weather = "cced0bc6133666f728728356fda52d60"
currency = CurrencyConverter()
amount = 0

@bot.message_handler(commands=['start','бастау','начать'])
def main(message):
    bot.send_message(message.chat.id,"Привет, ввидите сумму")
    bot.register_next_step_handler(message, summa)

def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат, впишите сумму')
        bot.register_next_step_handler(message, summa)
        return

    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
        btn4 = types.InlineKeyboardButton('другое значение', callback_data='else')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'Выберите пару валют', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Число должно быть больше за 0, впишите сумму")
        bot.register_next_step_handler(message, summa)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data != 'else':
        values = call.data.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f"Получается: {round(res, 2)}. Можете заново вписать сумму")
        bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.chat.id, "Введите пару значений через слеш")
        bot.register_next_step_handler(call.message, mycurrency)

def mycurrency(message):
    try:
        values = message.text.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f"Получается: {round(res, 2)}. Можете заново вписать сумму")
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(message.chat.id, "Что-то не так, впишите значение заново")
        bot.register_next_step_handler(message, mycurrency)


bot.polling(none_stop=True)