from telegram.ext import CommandHandler, MessageHandler, Filters, ConversationHandler
from .jobs import jobs
from datetime import datetime

def steps_inmet(dispatcher, message):
    content = {}
    filter_cancel = Filters.regex(r'\b(?:(?!cancelar)\w)+\b')
    
    get_time = lambda values : (list(filter(lambda i: len(i) > 1 and len(i) <= 2, values)) or [''])[0]
    get_date = lambda values : (list(filter(lambda i: len(i) == 8, values)) or [''])[0]
    time = lambda key, time : {key: '0{}:00'.format(time)} if len(time) == 1 else {key: '{}:00'.format(time)} if len(time) == 2 else {}
    date = lambda key, date : {key: datetime.strptime(date, '%d%m%Y').strftime('%Y-%m-%d')} if len(date) == 8 else {}

    def start(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=message['options']['info'])

        update.message.reply_text(message['options']['cities'])

        return 0

    def get_cities(update, context):
        content['station'] = update.message.text

        update.message.reply_text(message['options']['start'])

        return 1

    def get_start_event(update, context):
        user_input = update.message.text.split(' ', 2)

        content.update(time('hour_start', get_time(user_input)))
        content.update(date('date_start', get_date(user_input)))

        update.message.reply_text(message['options']['end'])
        
        return 2

    def get_end_event(update, context):
        user_input = update.message.text.split(' ', 2)

        content.update(time('hour_end', get_time(user_input)))
        content.update(date('date_end', get_date(user_input)))
            
        update.message.reply_text(message['options']['filter'])
        
        return 3

    def get_event(update, context):
        content['filter_by'] = list(map(lambda c : c.upper(), list(filter(lambda i : i.upper() in ['CHUVA', 'VENTO'], update.message.text.split(' ', 2))))) or ['CHUVA', 'VENTO']

        update.message.reply_text(message['options']['temperature'])
        
        return 4

    def get_aditional_info(update, context):
        content['enable_temp'] = True if update.message.text == 'sim' else False

        print(content)
        jobs(update, context, message, **content)
        
        return ConversationHandler.END
    
    def cancel(update, context):
        update.message.reply_text('Operação cancelada!')

        return ConversationHandler.END

    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex(r'4'), start,  pass_job_queue=True)],
        states={
            0: [MessageHandler(filter_cancel, get_cities)],
            1: [MessageHandler(filter_cancel, get_start_event)],
            2: [MessageHandler(filter_cancel, get_end_event)],
            3: [MessageHandler(filter_cancel, get_event)],
            4: [MessageHandler(filter_cancel, get_aditional_info)],
        },
        fallbacks=[MessageHandler(Filters.regex(r'cancelar'), cancel)],
    )
    
    dispatcher.add_handler(conv_handler)