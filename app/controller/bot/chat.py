import requests
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from ..cptec.make import make as cptec
from ..covid.make import make as covid
from ..alerts.make import make as alerts
from .messages import messages
import logging

__TOKEN = '1365811077:AAFXUgzOk9N9lissQ0-ikTlODc9Hc43qX2A'
__OPTIONS = {'cptec' : cptec, 'covid' : covid, 'alerts' : alerts}

def chat():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    def start(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=messages['welcome'])

    def report_weather(update, context):
        index = int(update.message.text) if update.message.text in [str(i) for i in range(1,10)] else 0

        if(index >= 1 and index <= len(__OPTIONS)):
            key = list(__OPTIONS.keys())[index - 1]
            context.bot.send_message(chat_id=update.effective_chat.id, text=messages['generate'][key])

            content = __OPTIONS[key]()

            for data in content:
                context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(data['file'], 'rb'), caption=data['message'])
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text=messages['unknown'])


    updater = Updater(token=__TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    report_weather = MessageHandler(Filters.text & (~Filters.command), report_weather)

    handlers = [start_handler, report_weather]

    for handle in handlers:
        dispatcher.add_handler(handle)

    updater.start_polling()
