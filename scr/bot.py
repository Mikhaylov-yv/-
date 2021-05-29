from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import time

import main

updater = Updater(token = '', use_context=True)

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text= 'Мы будем присылать данные об утечках топлива')
    d = main.Get_data()
    s = main.Resolution()
    while True:
        ur = d.get_data()
        signal = s.get_rez(ur)
        print(ur, signal)
        if signal:
            print('hy')
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text = f"В сосуде снизился уровень жидкости на {s.delta} л.")
        time.sleep(0.5)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()