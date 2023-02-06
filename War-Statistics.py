import telebot
from telebot import types
import LossesStaisticsOfrussia as rls

bot = telebot.TeleBot("5973837906:AAFJM4ql6YUXRHe-k2QDAUauY_TBiAdfLbc")

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
            harmaty = types.KeyboardButton('Гармати')
            ppo = types.KeyboardButton('Засоби ППО')
            bpla = types.KeyboardButton('БПЛА')
            avtomobiki = types.KeyboardButton('Автомобілі')
            rockets = types.KeyboardButton('Крилаті ракети')
            markup_reply.add(tanki, bbm, litaki, helicopteri, harmaty, ppo, bpla, avtomobiki, rockets)
            bot.send_message(call.message.chat.id, rls.personnel + ' ' +
            'станом на ' + rls.date,
            reply_markup = markup_reply, parse_mode='html')
        if call.data == 'dopomoga':
            bot.send_message(call.message.chat.id, 'Потрібна допомога?' + '\n' +
            'розробник - @nazarrudenok')

@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == 'Танки':
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
        bot.send_message(message.chat.id, rls.guns + ' ' +
        'станом на ' + rls.date)
    elif message.text == 'Засоби ППО':
        bot.send_message(message.chat.id, rls.ppo_means + ' ' +
        'станом на ' + rls.date)
    elif message.text == 'БПЛА':
        bot.send_message(message.chat.id, rls.drones + ' ' +
        'станом на ' + rls.date)
    elif message.text == 'Автомобілі':
        bot.send_message(message.chat.id, rls.cars + ' ' +
        'станом на ' + rls.date)
    elif message.text == 'Крилаті ракети':
        bot.send_message(message.chat.id, rls.rockets + ' ' +
        'станом на ' + rls.date)
    
bot.polling(none_stop=True)
