import requests
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from ..cptec.make import make as cptec
from ..covid.make import make as covid
from .messages import messages
import logging

__TOKEN = '1365811077:AAFXUgzOk9N9lissQ0-ikTlODc9Hc43qX2A'

def chat():
    updater = Updater(token=__TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    def start(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=messages['welcome'])

    def report_weather(update, context):
        if(update.message.text == '1'):
            
            context.bot.send_message(chat_id=update.effective_chat.id, text=messages['generate']['cptec'])

            for doc in cptec():
                context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(doc, 'rb'))
        elif(update.message.text == '2'):
            
            context.bot.send_message(chat_id=update.effective_chat.id, text=messages['generate']['covid'])

            for doc in covid():
                context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(doc, 'rb'))
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text=messages['unknown'])


    start_handler = CommandHandler('start', start)
    report_weather = MessageHandler(Filters.text & (~Filters.command), report_weather)

    handlers = [start_handler, report_weather]

    for handle in handlers:
        dispatcher.add_handler(handle)

    updater.start_polling()
