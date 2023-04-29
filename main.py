import telebot
from telebot import types
import fake_useragent
import requests
from bs4 import BeautifulSoup
from rus_statistics import *
from config import TOKEN

user = fake_useragent.UserAgent().random

headers_ = {
    'user-agent': user
}

url = 'https://russianwarship.rip/'
r = requests.get(url)

bs = BeautifulSoup(r.text, 'html.parser')

# def date_func():
#     url = 'https://www.minusrus.com/'
#     r = requests.get(url, headers=headers_)
#     bs = BeautifulSoup(r.text, 'html.parser')
#     date_ = bs.find('div', class_ = 'date').find('span').text
#     return date_

def personnell():
    total = bs.find('div', class_ = 'loses-item-title').find_all('span')[0].text.strip()
    return total

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
            warships_en = types.KeyboardButton('Warships')
            
            markup_reply.add(personnel_en, tanks_en, bbm_en, planes_en, helicopters_en, artillery_en, warships_en)


            bot.send_message(call.message.chat.id, 'I am a bot that informs people about the losses of Russia!')
            bot.send_message(call.message.chat.id, 'Select the button', reply_markup = markup_reply, parse_mode='html')
        
@bot.message_handler(content_types=['text'])
def text(message):
    mch = message.chat.id
    mt = message.text
    if mt == 'Особовий склад':
        bot.send_message(mch, f'Знищено особового складу: {personnel("total")}\nЗа останню добу: {personnel("quantity")}')
    elif mt == 'Танки':
        bot.send_message(mch, f'Знищено танків: {tanks("total")}\nЗа останню добу: {tanks("quantity")}')
    elif mt == 'ББМ':
        bot.send_message(mch, f'Знищено броньованих машин: {bbm("total")}\nЗа останню добу: {bbm("quantity")}')
    elif mt == 'Літаки':
        bot.send_message(mch, f'Знищено літаків: {planes("total")}\nЗа останню добу: {planes("quantity")}')
    elif mt == 'Гелікоптери':
        bot.send_message(mch, f'Знищено гелікоптерів: {helicopters("total")}\nЗа останню добу: {helicopters("quantity")}')
    elif mt == 'Артилерія':
        bot.send_message(mch, f'Знищено артилерійських установок: {artillery("total")}\nЗа останню добу: {artillery("quantity")}')
    elif mt == 'Кораблі':
        bot.send_message(mch, f'Знищено кораблів: {warships("total")}\nЗа останню добу: {warships("quantity")}')
    
    if mt == 'Personnel':
        bot.send_message(mch, f'Personnel were destroyed: {personnel("total")}\nFor the last day: {personnel("quantity")}')
    elif mt == 'Tanks':
        bot.send_message(mch, f'Tanks were destroyed: {tanks("total")}\nFor the last day: {tanks("quantity")}')
    elif mt == 'Armored vehicle':
        bot.send_message(mch, f'Armored vehicles were destroyed: {bbm("total")}\nFor the last day: {bbm("quantity")}')
    elif mt == 'Planes':
        bot.send_message(mch, f'Planes were destroyed: {planes("total")}\nFor the last day: {planes("quantity")}')
    elif mt == 'Helicopters':
        bot.send_message(mch, f'Helicopters were destroyed: {helicopters("total")}\nFor the last day: {helicopters("quantity")}')
    elif mt == 'Artillery':
        bot.send_message(mch, f'Artillery were destroyed: {artillery("total")}\nFor the last day: {artillery("quantity")}')
    elif mt == 'Warships':
        bot.send_message(mch, f'Warships were destroyed: {warships("total")}\nFor the last day: {warships("quantity")}')

bot.polling()