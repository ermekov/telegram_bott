import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('7083395817:AAF7QjavKj8QHWdYoLiX6xUqpSmSsFTPD48')

@bot.message_handler(commands=['start','бастау','начать'])
def main(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Перейти на сайт")
    markup.row(btn1)
    btn2 = types.KeyboardButton("Удалить фото")
    btn3 = types.KeyboardButton("Изменить текст")
    markup.row(btn2, btn3)
    file = open('./photo.jpg', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    #bot.send_message(message.chat.id, f"Салем :) {message.from_user.first_name}", reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == "Перейти на сайт":
        bot.send_message(message.chat.id, 'Website is open')
    elif message.text == "Удалить фото":
        bot.send_message(message.chat.id, 'Deleted')

@bot.message_handler(commands=['help','көмек','помочь'])
def main(message):
    bot.send_message(message.chat.id, "<b>Қандай жағдай туындады</b>, мәселені айта аласыз ба?", parse_mode="html")

@bot.message_handler(commands=['site','website'])
def site(message):
    webbrowser.open('https://github.com/ermekov/Resume/blob/main/Yermekov_Yerassyl_Res.pdf')

@bot.message_handler()
def info(message):
    if message.text.lower()=="салем":
        bot.send_message(message.chat.id,f'Салем, {message.from_user.first_name}')
    elif message.text.lower()=='id':
        bot.reply_to(message, f'ID: {message.from_user.id}')

@bot.message_handler(content_types=['photo'])
def photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Перейти на сайт", url='https://github.com/ermekov/Resume/blob/main/Yermekov_Yerassyl_Res.pdf')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton("Удалить фото", callback_data="delete")
    btn3 = types.InlineKeyboardButton("Изменить текст", callback_data="edit")
    markup.row(btn2, btn3)
    bot.reply_to(message, "Жақсы сурет :)", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data=="delete":
        bot.delete_message(callback.message.chat.id, callback.message.message_id-1)
    elif callback.data=="edit":
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)

bot.polling(none_stop=True)