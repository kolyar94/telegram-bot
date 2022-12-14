
import random

import telebot
from telebot import types
token=''
bot=telebot.TeleBot(token)
sms=['Для возвращения на главное меню введите любое слово!']
kon1=['Записаться на маникюр или педикюр можно по телефону: '
     '+3753362686** ,или INSTAGRAM https://instagram.com/daria.y_nails?igshid=Ym*yMTA2M2Y=   ']
kon2=['Записаться на брови или ресницы можно по телефону:'
     '+375 ,либо написать в INSTAGRAM: https://instagram.com/browi_yanina?igshid=Ym*yMTA2M2Y=']

def create_keyboard():
    keyboard=types.InlineKeyboardMarkup()
    services_1_btn=types.InlineKeyboardButton(text='Прайс по маникюру и педикюру', callback_data='1')
    services_btn = types.InlineKeyboardButton(text='Прайс по бровям и ресницам', callback_data='2')
    masters_btn = types.InlineKeyboardButton(text='Мастера', callback_data='3')
    sign_up_btn=types.InlineKeyboardButton(text='Записаться на маникюр или педикюр',callback_data='4')
    sign_up_1_btn=types.InlineKeyboardButton(text='Записаться на брови или ресницы',callback_data='5')

    keyboard.add(services_1_btn)
    keyboard.add(services_btn)
    keyboard.add(sign_up_btn)
    keyboard.add(sign_up_1_btn)
    keyboard.add(masters_btn)
    return keyboard
@bot.message_handler(content_types=['text'])
def start_bot(message):
    keyboard=create_keyboard()
    bot.send_message(
        message.chat.id,'Здравствуйте! Вас приветствует студия красоты TIME! ',
        reply_markup=keyboard
        )

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    keyboard=create_keyboard()
    if call.message:
        if call.data=='1':
            img = open('пра.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Прайс по маникюру и педикюру')
            msg = random.choice(sms)
            bot.send_message(call.message.chat.id, msg)

        if call.message:
            if call.data == '2':
                img = open('прайс брови.jpg', 'rb')
                bot.send_photo(
                    chat_id=call.message.chat.id,
                    photo=img,
                    caption='Прайс по бровям и ресницам')
                msg = random.choice(sms)
                bot.send_message(call.message.chat.id, msg)
        if call.data == '3':
          img = open('Даша.jpg', 'rb')
          bot.send_photo(
             chat_id=call.message.chat.id,
             photo=img,
             caption='Мастер по маникюру Даша')
          img = open('Янина.jpg','rb')
          bot.send_photo(
              chat_id=call.message.chat.id,
              photo=img,
              caption='Мастер по бровям Янина')
          msg = random.choice(sms)
          bot.send_message(call.message.chat.id, msg)
        if call.data == '4':
           msg = random.choice(kon1)
           bot.send_message(call.message.chat.id, msg)
           msg = random.choice(sms)
           bot.send_message(call.message.chat.id, msg)

        if call.data == '5':
           msg = random.choice(kon2)
           bot.send_message(call.message.chat.id, msg)
           msg = random.choice(sms)
           bot.send_message(call.message.chat.id, msg)




if __name__=='__main__':
  bot.polling(none_stop=True)