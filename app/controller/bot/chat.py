from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import ParseMode
from ..proxy import parallel
from ..alerts import alerts
from .messages import messages
import logging
import datetime

__TOKEN = '1365811077:AAFXUgzOk9N9lissQ0-ikTlODc9Hc43qX2A'
__MINUTES = 120
__TIMEOUT = 300


def chat():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    def start(update, context):
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=messages['welcome'])

    def notify(context):
        responses = alerts()

        if(responses):
            for reponse in responses:
                context.bot.send_photo(chat_id=context.job.context, photo=open(
                    reponse['file'], 'rb'), caption=reponse['message'], parse_mode=ParseMode.HTML, timeout=__TIMEOUT)

    def report_weather(update, context):
        key = update.message.text
        
        generate = messages['generate'][key] if key in messages['generate'] else None

        if(generate):
            if(key == '3'):
                status = {'status': 'Habilitado', 'bool': True} if not context.job_queue.jobs(
                ) else {'status': 'Desabilitado', 'bool': False}

                context.bot.send_message(
                    chat_id=update.effective_chat.id, text=(generate['message'] + status['status']))

                if(status['bool']):
                    context.job_queue.run_repeating(
                        callback=notify, interval=__MINUTES, context=update.message.chat_id)
                else:
                    context.job_queue.stop()

            else:
                context.bot.send_message(chat_id=update.effective_chat.id, text=generate['message'])

                content = parallel(generate['function'])

                for data in content:
                    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(data, 'rb'), timeout=__TIMEOUT)
        else: 
            context.bot.send_message(chat_id=update.effective_chat.id, text=messages['unknown'])
            
    updater = Updater(token=__TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    report_weather = MessageHandler(Filters.text & (
        ~Filters.command), report_weather, pass_job_queue=True)

    for handle in [start_handler, report_weather]:
        dispatcher.add_handler(handle)

    updater.start_polling()
