import telebot
bot = telebot.TeleBot('1244119215:AAEoOL8B8lSMbrJseOYzFnvAi6BIoyqcQBE')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Привет', 'Пока', 'Класс')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне/start',
                     reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, пользователь')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока, пользователь')
    elif message.text.lower() == 'класс':
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAIdX199zTMSVxbvn47G472JuBk1GqKnAAL2CgACLw_wBq2SsEybxHZXGwQ')


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)
bot.polling()