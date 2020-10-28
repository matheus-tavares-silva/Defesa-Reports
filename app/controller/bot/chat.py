from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import ParseMode
from ..proxy import parallel
from ..alerts import alerts
from ...env import telegram
from .jobs import jobs
import logging
import datetime

def chat():
    messages = telegram['messages']

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    def start(update, context):
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=messages['welcome'])

    def report(update, context):
        key = update.message.text
        
        content = messages['generate'][key] if key in messages['generate'] else None

        if(content):
            jobs(update, context, content)
        else: 
            context.bot.send_message(chat_id=update.effective_chat.id, text=messages['unknown'])
            
    updater = Updater(token=telegram['token'], use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    report = MessageHandler(Filters.text & (~Filters.command), report, pass_job_queue=True)

    for handle in [start_handler, report]:
        dispatcher.add_handler(handle)

    updater.start_polling()
