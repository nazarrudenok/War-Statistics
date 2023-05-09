import telebot
from telebot import types
import fake_useragent
import requests
from bs4 import BeautifulSoup
from RussianLosses import *
from config import TOKEN
from func import losses_detaited

user = fake_useragent.UserAgent().random

headers_ = {
    'user-agent': user
}

url = 'https://russianwarship.rip/'
r = requests.get(url)

bs = BeautifulSoup(r.text, 'html.parser')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width = 2)
    UA = types.InlineKeyboardButton('🇺🇦', callback_data = 'ukraine')
    EN = types.InlineKeyboardButton('🇺🇸', callback_data = 'america')
    markup.add(UA, EN)
    bot.send_message(message.chat.id, 'Вітаю! Обери мову\nCongratulations! Choose a language', reply_markup = markup)

@bot.message_handler(commands=['detailed_stats'])
def detailed(message):
    cht = message.chat.id
    bot.send_message(cht, 'Будь ласка, надішли дату за зразком: YYYY.MM.DD (2023.01.01)')

@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'ukraine':
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
            
            personnel = types.KeyboardButton('Особовий склад')
            tanks = types.KeyboardButton('Танки')
            armoured_fighting_vehicles = types.KeyboardButton('ББМ')
            planes = types.KeyboardButton('Літаки')
            helicopters = types.KeyboardButton('Гелікоптери')
            artillery = types.KeyboardButton('Артилерія')
            warships = types.KeyboardButton('Кораблі')

            markup_reply.add(personnel, tanks, armoured_fighting_vehicles, planes, helicopters, artillery, warships)

            bot.send_message(call.message.chat.id, 'Я - Бот, що інформує людей про втрати руzzні!')
            bot.send_message(call.message.chat.id, 'Обери кнопку', reply_markup = markup_reply, parse_mode='html')

        if call.data == 'america':
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
            
            personnel_en = types.KeyboardButton('Personnel')
            tanks_en = types.KeyboardButton('Tanks')
            armoured_fighting_vehicles_en = types.KeyboardButton('Armored vehicle')
            planes_en = types.KeyboardButton('Planes')
            helicopters_en = types.KeyboardButton('Helicopters')
            artillery_en = types.KeyboardButton('Artillery')
            warships_en = types.KeyboardButton('Warships')
            
            markup_reply.add(personnel_en, tanks_en, armoured_fighting_vehicles_en, planes_en, helicopters_en, artillery_en, warships_en)


            bot.send_message(call.message.chat.id, 'I am a bot that informs people about the losses of Russia!')
            bot.send_message(call.message.chat.id, 'Select the button', reply_markup = markup_reply, parse_mode='html')
        
@bot.message_handler(content_types=['text'])
def text(message):
    cht = message.chat.id
    mt = message.text
    if mt == 'Особовий склад':
        bot.send_message(cht, f'Станом на {date()}, {day()} день війни\nЗнищено особового складу: {personnel("total")}\nЗа останню добу: {personnel("quantity")}')
    elif mt == 'Танки':
        bot.send_message(cht, f'Станом на {date()}, {day()} день війни\nЗнищено танків: {tanks("total")}\nЗа останню добу: {tanks("quantity")}')
    elif mt == 'ББМ':
        bot.send_message(cht, f'Станом на {date()}, {day()} день війни\nЗнищено броньованих машин: {armoured_fighting_vehicles("total")}\nЗа останню добу: {armoured_fighting_vehicles("quantity")}')
    elif mt == 'Літаки':
        bot.send_message(cht, f'Станом на {date()}, {day()} день війни\nЗнищено літаків: {planes("total")}\nЗа останню добу: {planes("quantity")}')
    elif mt == 'Гелікоптери':
        bot.send_message(cht, f'Станом на {date()}, {day()} день війни\nЗнищено гелікоптерів: {helicopters("total")}\nЗа останню добу: {helicopters("quantity")}')
    elif mt == 'Артилерія':
        bot.send_message(cht, f'Станом на {date()}, {day()} день війни\nЗнищено артилерійських установок: {artillery_systems("total")}\nЗа останню добу: {artillery_systems("quantity")}')
    elif mt == 'Кораблі':
        bot.send_message(cht, f'Станом на {date()}, {day()} день війни\nЗнищено кораблів: {warships("total")}\nЗа останню добу: {warships("quantity")}')
    elif '.' in mt:
        mt = mt.replace('.', '-')
        bot.send_message(cht, losses_detaited(mt))

    if mt == 'Personnel':
        bot.send_message(cht, f'As of {date()}, {day()} day of war\nPersonnel were destroyed: {personnel("total")}\nFor the last day: {personnel("quantity")}')
    elif mt == 'Tanks':
        bot.send_message(cht, f'As of {date()}, {day()} day of war\nTanks were destroyed: {tanks("total")}\nFor the last day: {tanks("quantity")}')
    elif mt == 'Armored vehicle':
        bot.send_message(cht, f'As of {date()}, {day()} day of war\nArmored vehicles were destroyed: {armoured_fighting_vehicles("total")}\nFor the last day: {armoured_fighting_vehicles("quantity")}')
    elif mt == 'Planes':
        bot.send_message(cht, f'As of {date()}, {day()} day of war\nPlanes were destroyed: {planes("total")}\nFor the last day: {planes("quantity")}')
    elif mt == 'Helicopters':
        bot.send_message(cht, f'As of {date()}, {day()} day of war\nHelicopters were destroyed: {helicopters("total")}\nFor the last day: {helicopters("quantity")}')
    elif mt == 'Artillery':
        bot.send_message(cht, f'As of {date()}, {day()} day of war\nArtillery were destroyed: {artillery_systems("total")}\nFor the last day: {artillery_systems("quantity")}')
    elif mt == 'Warships':
        bot.send_message(cht, f'As of {date()}, {day()} day of war\nWarships were destroyed: {warships("total")}\nFor the last day: {warships("quantity")}')

bot.polling()