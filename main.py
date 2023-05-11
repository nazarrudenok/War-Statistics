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
    bot.send_message(cht, 'Будь ласка, надішли дату за зразком:\nYYYY.MM.DD ua/en\n2023.01.01 ua/en')

@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'ukraine':
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
            
            personnel = types.KeyboardButton('Особовий склад')
            tanks = types.KeyboardButton('Танки')
            armoured_fighting_vehicles = types.KeyboardButton('ББМ')
            artillery = types.KeyboardButton('Артилерія')
            mlrs = types.KeyboardButton('РСЗВ')
            aa_warfare_systems = types.KeyboardButton('Засоби ППО')
            planes = types.KeyboardButton('Літаки')
            helicopters = types.KeyboardButton('Гелікоптери')
            vehicles_fuel_tanks = types.KeyboardButton('Автомобілі')
            warships = types.KeyboardButton('Кораблі')
            uav_systems = types.KeyboardButton('БПЛА')
            cruise_missiles = types.KeyboardButton('Крилаті ракети')
            special_military_equip = types.KeyboardButton('Спеціальна техніка')
            atgm_srbm_systems = types.KeyboardButton('Балістичні ракети')

            markup_reply.add(personnel,
                             tanks,
                             armoured_fighting_vehicles,
                             planes, helicopters, artillery,
                             warships, mlrs, aa_warfare_systems,
                             vehicles_fuel_tanks,
                             uav_systems, cruise_missiles,
                             special_military_equip,
                             atgm_srbm_systems)

            bot.send_message(call.message.chat.id, 'Я - Бот, що інформує людей про втрати руzzні!')
            bot.send_message(call.message.chat.id, 'Обери кнопку', reply_markup = markup_reply, parse_mode='html')

        if call.data == 'america':
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
            
            personnel_en = types.KeyboardButton('Personnel')
            tanks_en = types.KeyboardButton('Tanks')
            armoured_fighting_vehicles_en = types.KeyboardButton('Armored vehicle')
            artillery_en = types.KeyboardButton('Artillery')
            mlrs_en = types.KeyboardButton('MLRS')
            aa_warfare_systems_en = types.KeyboardButton('Anti-aircraft warfare')
            planes_en = types.KeyboardButton('Planes')
            helicopters_en = types.KeyboardButton('Helicopters')
            vehicles_fuel_tanks_en = types.KeyboardButton('Cars')
            warships_en = types.KeyboardButton('Warships')
            uav_systems_en = types.KeyboardButton('UAV')
            cruise_missiles_en = types.KeyboardButton('Cruise missiles')
            special_military_equip_en = types.KeyboardButton('Special equipment')
            atgm_srbm_systems_en = types.KeyboardButton('ATGM-SRBM systems')
            
            markup_reply.add(personnel_en,
                             tanks_en,
                             armoured_fighting_vehicles_en,
                             planes_en,
                             helicopters_en,
                             artillery_en,
                             warships_en,
                             mlrs_en,
                             vehicles_fuel_tanks_en,
                             uav_systems_en,
                             cruise_missiles_en,
                             special_military_equip_en,
                             aa_warfare_systems_en,
                             atgm_srbm_systems_en)


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
    elif mt == 'РСЗВ':
        bot.send_message(cht, f'Станом на {date()}, {day()} день війни\nЗнищено реактивних систем залпоаого вогню: {mlrs("total")}\nЗа останню добу: {mlrs("quantity")}')
    elif mt == 'Засоби ППО':
        bot.send_message(cht, f'Станом на {date()}, {day()} день війни\nЗнищено засобів ППО: {aa_warfare_systems("total")}\nЗа останню добу: {aa_warfare_systems("quantity")}')
    elif mt == 'Автомобілі':
        bot.send_message(cht, f'Станом на {date()}, {day()} день війни\nЗнищено автомобілів та цистерн: {vehicles("total")}\nЗа останню добу: {vehicles("quantity")}')
    elif mt == 'БПЛА':
        bot.send_message(cht, f'Станом на {date()}, {day()} день війни\nЗнищено безпілотників: {uav_systems("total")}\nЗа останню добу: {uav_systems("quantity")}')
    elif mt == 'Крилаті ракети':
        bot.send_message(cht, f'Станом на {date()}, {day()} день війни\nЗнищено крилатих ракет: {cruise_missiles("total")}\nЗа останню добу: {cruise_missiles("quantity")}')
    elif mt == 'Спеціальна техніка':
        bot.send_message(cht, f'Станом на {date()}, {day()} день війни\nЗнищено спеціальної техніки: {special_military_equip("total")}\nЗа останню добу: {special_military_equip("quantity")}')
    elif mt == 'Балістичні ракети':
        bot.send_message(cht, f'Станом на {date()}, {day()} день війни\nЗнищено балістичних ракет: {atgm_srbm_systems("total")}\nЗа останню добу: {atgm_srbm_systems("quantity")}')
    elif '.' and 'ua' in mt:
        mt = mt.replace('.', '-')
        mt = mt[:10]
        bot.reply_to_message(cht, losses_detaited(mt))
    else:
        bot.send_message(cht, 'Я не розумію цієї команди')

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
    elif mt == 'MLRS':
        bot.send_message(cht, f'As of {date()}, {day()} day of war\nMLRS were destroyed: {mlrs("total")}\nFor the last day: {mlrs("quantity")}')
    elif mt == 'Cars':
        bot.send_message(cht, f'As of {date()}, {day()} day of war\nCars and cisterns were destroyed: {vehicles("total")}\nFor the last day: {vehicles("quantity")}')
    elif mt == 'UAV':
        bot.send_message(cht, f'As of {date()}, {day()} day of war\nDrones were destroyed: {uav_systems("total")}\nFor the last day: {uav_systems("quantity")}')
    elif mt == 'Cruise missiles':
        bot.send_message(cht, f'As of {date()}, {day()} day of war\nCruise missiles were destroyed: {cruise_missiles("total")}\nFor the last day: {cruise_missiles("quantity")}')
    elif mt == 'Special equipment':
        bot.send_message(cht, f'As of {date()}, {day()} day of war\nSpecial equipment were destroyed: {special_military_equip("total")}\nFor the last day: {special_military_equip("quantity")}')
    elif mt == 'Anti-aircraft warfare':
        bot.send_message(cht, f'As of {date()}, {day()} day of war\nAnti-aircraft warface were destroyed: {aa_warfare_systems("total")}\nFor the last day: {aa_warfare_systems("quantity")}')
    elif mt == 'ATGM-SRBM systems':
        bot.send_message(cht, f'As of {date()}, {day()} day of war\nATGM-SRBM systems were destroyed: {atgm_srbm_systems("total")}\nFor the last day: {atgm_srbm_systems("quantity")}')
    elif '.' and 'en' in mt:
        # bot.send_message(cht, losses_detaited(mt))
        bot.send_message(cht, 'Ця функція поки що не доступна')

bot.polling()
