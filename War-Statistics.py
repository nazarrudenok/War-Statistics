import telebot
from telebot import types
import lossesofrussia as rls

bot = telebot.TeleBot("5973837906:AAFJM4ql6YUXRHe-k2QDAUauY_TBiAdfLbc")


@bot.message_handler(commands = ["start"])
def start(message):        
    markup = types.InlineKeyboardMarkup(row_width = 2)
    sho_po_rusni = types.InlineKeyboardButton('🇺🇦', callback_data = 'ukraine')
    dopomoga = types.InlineKeyboardButton('🇺🇸', callback_data = 'america')
    markup.add(sho_po_rusni, dopomoga)
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
