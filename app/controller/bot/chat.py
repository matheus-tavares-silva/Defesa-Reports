import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from ..cptec.make import make as cptec
from ..covid.make import make as covid
from ..alerts import alerts
from .messages import messages
import logging
import datetime

__TOKEN = '1365811077:AAFXUgzOk9N9lissQ0-ikTlODc9Hc43qX2A'
__OPTIONS = {'cptec' : cptec, 'covid' : covid, 'alerts' : alerts}
__MINUTES = 150

def chat():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    def start(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=messages['welcome'])

    def notify(context):
        responses = __OPTIONS['alerts']()

        if(len(responses) > 0):
            for reponse in responses:
                context.bot.send_photo(chat_id=context.job.context, photo=open(reponse['file'], 'rb'), caption=reponse['message'])


    def report_weather(update, context):
        index = int(update.message.text) if update.message.text in [str(i) for i in range(1,10)] else 0

        if(index >= 1 and index <= len(__OPTIONS)):
            key = list(__OPTIONS.keys())[index - 1]
            text = messages['generate'][key]

            content = __OPTIONS[key]()
            
            if(key == 'alerts'):
                status = {'status' : 'Habilitado', 'bool' : True} if not context.job_queue.jobs() else {'status' : 'Desabilitado', 'bool' : False}

                context.bot.send_message(chat_id=update.effective_chat.id, text=(text + status['status']))

                if(status['bool']):
                    context.job_queue.run_repeating(callback=notify, interval=__MINUTES, context=update.message.chat_id)
                else:
                    context.job_queue.stop()
                
            else:
                context.bot.send_message(chat_id=update.effective_chat.id, text=text)

                for data in content:
                    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(data['file'], 'rb'), caption=data['message'])
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text=messages['unknown'])

    updater = Updater(token=__TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    report_weather = MessageHandler(Filters.text & (~Filters.command), report_weather, pass_job_queue=True)

    for handle in [start_handler, report_weather]:
        dispatcher.add_handler(handle)

    updater.start_polling()

