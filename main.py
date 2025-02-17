import telebot
import webbrowser

bot = telebot.TeleBot('7083395817:AAF7QjavKj8QHWdYoLiX6xUqpSmSsFTPD48')

@bot.message_handler(commands=['start','бастау','начать'])
def main(message):
    bot.send_message(message.chat.id, f"Салем :) {message.from_user.first_name}")

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
bot.polling(none_stop=True)