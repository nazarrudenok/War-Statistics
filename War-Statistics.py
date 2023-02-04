import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
import time

bot = telebot.TeleBot("5973837906:AAFJM4ql6YUXRHe-k2QDAUauY_TBiAdfLbc")

url = 'https://zp.gov.ua/ru/articles/item/16921/vtrati-voroga-zrostayut'
response = requests.get(url)
bs = BeautifulSoup(response.text, 'html.parser')

time_str = time.strftime('%d.%m.%Y.%s')


russian_items = bs.find('div', class_ = 'page-content content-text').find_all('p')

@bot.message_handler(commands = ["help"])
def help(message):
    bot.send_message(message.chat.id, "Маєте зауваження?\nРозробник - @nazarrudenok")

@bot.message_handler(commands = ["start"])
def start(message):        
    markup = types.InlineKeyboardMarkup(row_width = 2)
    sho_po_rusni = types.InlineKeyboardButton('Шо по русні?👹', callback_data = 'markups')
    dopomoga = types.InlineKeyboardButton('Допомога', callback_data = 'dopomoga')
    markup.add(sho_po_rusni, dopomoga)
    bot.send_message(message.chat.id, 'Вітаю,' f'<b>{message.from_user.first_name}</b>!''\nЯ - Бот, що інформує людей про втрати руzzні!', reply_markup = markup, parse_mode = 'html')

@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'markups':
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
            tanki = types.KeyboardButton('Танки')
            bbm = types.KeyboardButton('ББМ')
            litaki = types.KeyboardButton('Літаки')
            helicopteri = types.KeyboardButton('Гелікоптери')
            harmaty = types.KeyboardButton('Артилерійські системи')
            ppo = types.KeyboardButton('Засоби ППО')
            bpla = types.KeyboardButton('БПЛА')
            avtomobiki = types.KeyboardButton('Автомобілі')
            rockets = types.KeyboardButton('Крилаті ракети')
            markup_reply.add(tanki, bbm, litaki, helicopteri, harmaty, ppo, bpla, avtomobiki, rockets)
            bot.send_message(call.message.chat.id, russian_items[1].text + ' ' +
            'станом на ' + time_str,
            reply_markup = markup_reply, parse_mode='html')
        if call.data == 'dopomoga':
            bot.send_message(call.message.chat.id, 'Потрібна допомога?' + '\n' +
            'розробник - @nazarrudenok')

@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == 'Танки':
        bot.send_message(message.chat.id, russian_items[2].text + ' ' +
        'станом на ' + time_str)
    elif message.text == 'ББМ':
        bot.send_message(message.chat.id, russian_items[3].text + ' ' +
        'станом на ' + time_str)
    elif message.text == 'Літаки':
        bot.send_message(message.chat.id, russian_items[7].text + ' ' +
        'станом на ' + time_str)
    elif message.text == 'Гелікоптери':
        bot.send_message(message.chat.id, russian_items[8].text + ' ' +
        'станом на ' + time_str)
    elif message.text == 'Артилерійські системи':
        bot.send_message(message.chat.id, russian_items[4].text + ' ' +
        'станом на ' + time_str)
    elif message.text == 'Засоби ППО':
        bot.send_message(message.chat.id, russian_items[6].text + ' ' +
        'станом на ' + time_str)
    elif message.text == 'БПЛА':
        bot.send_message(message.chat.id, russian_items[9].text + ' ' +
        'станом на ' + time_str)
    elif message.text == 'Автомобілі':
        bot.send_message(message.chat.id, russian_items[13].text + ' ' +
        'станом на ' + time_str)
    elif message.text == 'Крилаті ракети':
        bot.send_message(message.chat.id, russian_items[10].text + ' ' +
        'станом на ' + time_str)
    
bot.polling(none_stop=True)
