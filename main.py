import telebot
from telebot import types
import fake_useragent
import requests
import time
from bs4 import BeautifulSoup
# from RussianLosses import *
from config import TOKEN

user = fake_useragent.UserAgent().random

headers_ = {
    'user-agent': user
}

url = 'https://www.minusrus.com/'
r = requests.get(url)

bs = BeautifulSoup(r.text, 'html.parser')

def personnel(item):
    total = bs.find('div', class_ = 'card__amount').find_all('span')[0].text.replace('.', ' ').replace('~', '').strip()
    quantity = bs.find('div', class_ = 'card__amount').find_all('span')[1].text.strip()
    if item == 'total':
        return total
    elif item == 'quantity':
        return quantity
    else:
        error = 'error: invalid argument'
        return error

# def date_func():
#     url = 'https://www.minusrus.com/'
#     r = requests.get(url, headers=headers_)
#     bs = BeautifulSoup(r.text, 'html.parser')
#     date_ = bs.find('div', class_ = 'date').find('span').text
#     return date_

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width = 2)
    UA = types.InlineKeyboardButton('🇺🇦', callback_data = 'ukraine')
    EN = types.InlineKeyboardButton('🇺🇸', callback_data = 'america')
    markup.add(UA, EN)
    bot.send_message(message.chat.id, 'Вітаю! Обери мову\nCongratulations! Choose a language', reply_markup = markup)

@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'ukraine':
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
            
            personnel = types.KeyboardButton('Особовий склад')
            tanks = types.KeyboardButton('Танки')
            bbm = types.KeyboardButton('ББМ')
            planes = types.KeyboardButton('Літаки')
            helicopters = types.KeyboardButton('Гелікоптери')
            artillery = types.KeyboardButton('Артилерія')
            warships = types.KeyboardButton('Кораблі')

            markup_reply.add(personnel, tanks, bbm, planes, helicopters, artillery, warships)

            bot.send_message(call.message.chat.id, 'Я - Бот, що інформує людей про втрати руzzні!')
            bot.send_message(call.message.chat.id, 'Обери кнопку', reply_markup = markup_reply, parse_mode='html')

        if call.data == 'america':
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
            
            personnel_en = types.KeyboardButton('Personnel')
            tanks_en = types.KeyboardButton('Tanks')
            bbm_en = types.KeyboardButton('Armored vehicle')
            planes_en = types.KeyboardButton('Planes')
            helicopters_en = types.KeyboardButton('Helicopters')
            artillery_en = types.KeyboardButton('Artillery')
            warships_en = types.KeyboardButton('Ships')
            
            markup_reply.add(personnel_en, tanks_en, bbm_en, planes_en, helicopters_en, artillery_en, warships_en)


            bot.send_message(call.message.chat.id, 'I am a bot that informs people about the losses of Russia!')
            bot.send_message(call.message.chat.id, 'Select the button', reply_markup = markup_reply, parse_mode='html')
        
@bot.message_handler(content_types=['text'])
def text(message):
    mch = message.chat.id
    mt = message.text
    if mt == 'Особовий склад':
        bot.send_message(mch, 'asd')
        while True:
            print(personnel('total'))
            time.sleep(3)
bot.polling()