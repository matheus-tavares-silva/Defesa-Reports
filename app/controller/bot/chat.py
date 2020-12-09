from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler
from telegram import ReplyKeyboardRemove
from ...env import telegram
from .jobs import jobs
from .conversation import steps_inmet, steps_local_report
import logging
import datetime

def chat():
    messages = telegram['messages']
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)   
    service = lambda key :  messages['generate'][key] if key in messages['generate'] else None

    def start(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=messages['welcome'])    

    def report(update, context):
        content = service(update.message.text)

        if(content):
            jobs(update, context, content)
        else:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=messages['unknown'])

    updater = Updater(token=telegram['token'], use_context=True)
    dispatcher = updater.dispatcher
    report_handler = MessageHandler(Filters.text, report,  pass_job_queue=True)
    start_handler = CommandHandler('start', start)

    steps_inmet(dispatcher, service('4'))
    steps_local_report(dispatcher, service('6'))

    for handle in [
        start_handler, 
        report_handler,
    ]:
        dispatcher.add_handler(handle)

    updater.start_polling()
