import telebot
from telebot import types
import lossesofrussia as rls
import requests
import datetime
import time
import pytz

bot = telebot.TeleBot("5973837906:AAFJM4ql6YUXRHe-k2QDAUauY_TBiAdfLbc")

tz = pytz.timezone('Europe/Kiev')

@bot.message_handler(commands = ["start"])
def start(message):        
    markup = types.InlineKeyboardMarkup(row_width = 2)
    sho_po_rusni = types.InlineKeyboardButton('🇺🇦', callback_data = 'ukraine')
    dopomoga = types.InlineKeyboardButton('🇺🇸', callback_data = 'america')
    markup.add(sho_po_rusni, dopomoga)
    bot.send_message(message.chat.id, 'Вітаю! Обери мову\nCongratulations! Choose a language\n\nІнформація про повітряні тривоги - /air_alarms', reply_markup = markup)


    # while True:
    #     current_time = datetime.datetime.now(tz)
    #     if current_time.hour == 9 and current_time.minute == 0:
    #         bot.send_message(chat_id=message.chat.id, text="Добрий ранок! Втрати за минулу добу:\n" + rls.personnel)
    #     time.sleep(60)


@bot.message_handler(commands=['air_alarms'])
def alarms(message):
    headers = {'X-API-Key': '52b9d358bcb491a92d2ba114fd07dde825961358'}
    response = requests.get('https://alerts.com.ua/api/states', headers = headers)
    
    alarm_json = response.json()
    
    alarm_vinnytsia = alarm_json['states'][0]['alert']
    alarm_volyn = alarm_json['states'][1]['alert']
    alarm_dnipro = alarm_json['states'][2]['alert']
    alarm_donbas = alarm_json['states'][3]['alert']
    alarm_zhytomyr = alarm_json['states'][4]['alert']
    alarm_karpaty = alarm_json['states'][5]['alert']
    alarm_zaporizhya = alarm_json['states'][6]['alert']
    alarm_franik = alarm_json['states'][7]['alert']
    alarm_kyiv_obl = alarm_json['states'][8]['alert']
    alarm_kirovograd = alarm_json['states'][9]['alert']
    alarm_lugansk = alarm_json['states'][10]['alert']
    alarm_lviv = alarm_json['states'][11]['alert']
    alarm_mykolaiv = alarm_json['states'][12]['alert']
    alarm_odessa = alarm_json['states'][13]['alert']
    alarm_poltava = alarm_json['states'][14]['alert']
    alarm_rivne = alarm_json['states'][15]['alert']
    alarm_sumy = alarm_json['states'][16]['alert']
    alarm_ternopil = alarm_json['states'][17]['alert']
    alarm_kharkiv = alarm_json['states'][18]['alert']
    alarm_kherson = alarm_json['states'][19]['alert']
    alarm_khmel = alarm_json['states'][20]['alert']
    alarm_cherkasy = alarm_json['states'][21]['alert']
    alarm_chernivtsy = alarm_json['states'][22]['alert']
    alarm_chernihiv = alarm_json['states'][23]['alert']
    alarm_kyiv = alarm_json['states'][24]['alert']


    if alarm_vinnytsia:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][0]['name'])
    if alarm_volyn:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][1]['name'])
    if alarm_dnipro:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][2]['name'])
    if alarm_donbas:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][3]['name'])
    if alarm_zhytomyr:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][4]['name'])
    if alarm_karpaty:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][5]['name'])
    if alarm_zaporizhya:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][6]['name'])
    if alarm_franik:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][7]['name'])
    if alarm_kyiv_obl:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][8]['name'])
    if alarm_kirovograd:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][9]['name'])
    if alarm_lugansk:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][10]['name'])
    if alarm_lviv:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][11]['name'])
    if alarm_mykolaiv:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][12]['name'])
    if alarm_odessa:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][13]['name'])
    if alarm_poltava:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][14]['name'])
    if alarm_rivne:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][15]['name'])
    if alarm_sumy:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][16]['name'])
    if alarm_ternopil:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][17]['name'])
    if alarm_kharkiv:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][18]['name'])
    if alarm_kherson:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][19]['name'])
    if alarm_khmel:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][20]['name'])
    if alarm_cherkasy:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][21]['name'])
    if alarm_chernivtsy:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][22]['name'])
    if alarm_chernihiv:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][23]['name'])
    if alarm_kyiv:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][24]['name'])
        

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
            guns = types.KeyboardButton('Гармати')
            ppo_means = types.KeyboardButton('Засоби ППО')
            drones = types.KeyboardButton('БПЛА')
            cars = types.KeyboardButton('Автомобілі')
            rockets = types.KeyboardButton('Крилаті ракети')
            warships = types.KeyboardButton('Кораблі')
            special_equipment = types.KeyboardButton('Спеціальна техніка')
            
            markup_reply.add(personnel, tanks, bbm, planes, helicopters, guns, ppo_means, drones, cars, rockets, warships, special_equipment)

            bot.send_message(call.message.chat.id, 'Я - Бот, що інформує людей про втрати руzzні!')

            bot.send_message(call.message.chat.id, 'Обери кнопку', reply_markup = markup_reply, parse_mode='html')

        if call.data == 'america':
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
            
            personnel_en = types.KeyboardButton('Personnel')
            tanks_en = types.KeyboardButton('Tanks')
            bbm_en = types.KeyboardButton('Armored vehicle')
            planes_en = types.KeyboardButton('Planes')
            helicopters_en = types.KeyboardButton('Helicopters')
            guns_en = types.KeyboardButton('Cannons')
            ppo_means_en = types.KeyboardButton('Anti-aircraft warfare')
            drones_en = types.KeyboardButton('UAV')
            cars_en = types.KeyboardButton('Cars')
            rockets_en = types.KeyboardButton('Cruise missiles')
            warships_en = types.KeyboardButton('Ships')
            special_equipment_en = types.KeyboardButton('Special equipment')
            
            markup_reply.add(personnel_en, tanks_en, bbm_en, planes_en, helicopters_en, guns_en, ppo_means_en, drones_en, cars_en, rockets_en, warships_en, special_equipment_en)


            bot.send_message(call.message.chat.id, 'I am a bot that informs people about the losses of Russia!')
            bot.send_message(call.message.chat.id, 'Select the button', reply_markup = markup_reply, parse_mode='html')



@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == 'Особовий склад':
        bot.send_message(message.chat.id, rls.personnel + ' ' +
        'станом на ' + rls.date)
    elif message.text == 'Танки':
        bot.send_message(message.chat.id, rls.tanks + ' ' +
        'станом на ' + rls.date)
    elif message.text == 'ББМ':
        bot.send_message(message.chat.id, rls.bbm + ' ' +
        'станом на ' + rls.date)
    elif message.text == 'Літаки':
        bot.send_message(message.chat.id,rls.planes + ' ' +
        'станом на ' + rls.date)
    elif message.text == 'Гелікоптери':
        bot.send_message(message.chat.id, rls.helicopters + ' ' +
        'станом на ' + rls.date)
    elif message.text == 'Гармати':
        bot.send_message(message.chat.id, rls.cannons + ' ' +
        'станом на ' + rls.date)
    elif message.text == 'Засоби ППО':
        bot.send_message(message.chat.id, rls.anti_aircraft_warfare + ' ' +
        'станом на ' + rls.date)
    elif message.text == 'БПЛА':
        bot.send_message(message.chat.id, rls.drones + ' ' +
        'станом на ' + rls.date)
    elif message.text == 'Автомобілі':
        bot.send_message(message.chat.id, rls.cars + ' ' +
        'станом на ' + rls.date)
    elif message.text == 'Крилаті ракети':
        bot.send_message(message.chat.id, rls.cruise_missiles + ' ' +
        'станом на ' + rls.date)
    elif message.text == 'Кораблі':
        bot.send_message(message.chat.id, rls.warships + ' ' +
        'станом на ' + rls.date)
    elif message.text == 'Спеціальна техніка':
        bot.send_message(message.chat.id, rls.special_equipment + ' ' +
        'станом на ' + rls.date)

    elif message.text == 'Personnel':
        bot.send_message(message.chat.id, rls.personnel_eng + ' ' +
        'as of ' + rls.date)
    elif message.text == 'Tanks':
        bot.send_message(message.chat.id, rls.tanks_eng + ' ' +
        'as of ' + rls.date)
    elif message.text == 'Armored vehicle':
        bot.send_message(message.chat.id, rls.bbm_eng + ' ' +
        'as of ' + rls.date)
    elif message.text == 'Planes':
        bot.send_message(message.chat.id,rls.planes_eng + ' ' +
        'as of ' + rls.date)
    elif message.text == 'Helicopters':
        bot.send_message(message.chat.id, rls.helicopters_eng + ' ' +
        'as of ' + rls.date)
    elif message.text == 'Cannons':
        bot.send_message(message.chat.id, rls.cannons_eng + ' ' +
        'as of ' + rls.date)
    elif message.text == 'Anti-aircraft warfare':
        bot.send_message(message.chat.id, rls.anti_aircraft_warfare_eng + ' ' +
        'as of ' + rls.date)
    elif message.text == 'UAV':
        bot.send_message(message.chat.id, rls.drones_eng + ' ' +
        'as of ' + rls.date)
    elif message.text == 'Cars':
        bot.send_message(message.chat.id, rls.cars_eng + ' ' +
        'as of ' + rls.date)
    elif message.text == 'Cruise missiles':
        bot.send_message(message.chat.id, rls.cruise_missiles_eng + ' ' +
        'as of ' + rls.date)
    elif message.text == 'Ships':
        bot.send_message(message.chat.id, rls.warships_eng + ' ' +
        'as of ' + rls.date)
    elif message.text == 'Special equipment':
        bot.send_message(message.chat.id, rls.special_equipment_eng + ' ' +
        'as of ' + rls.date)

    
bot.polling(none_stop=True)
