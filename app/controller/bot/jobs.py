from ..proxy import parallel
from telegram import ParseMode

def jobs(update, context, env, timeout=120, interval=120):

    chat_id = update.effective_chat.id
    message = context.bot.send_message
    queue = {
        'once' : context.job_queue.run_once,
        'repeater' : context.job_queue.run_repeating
    }

    def repeater(context):

        responses = parallel('alerts')

        if(responses):
            for reponse in responses:
                context.bot.send_photo(chat_id=context.job.context, photo=open(
                    reponse['file'], 'rb'), caption=reponse['warning'], parse_mode=ParseMode.HTML, timeout=timeout)

    def once(context):
        message(chat_id=chat_id, text=env['warning'])

        content = parallel(env['service'])

        message(chat_id=chat_id, text=env['success'])

        if(content):
            for data in content:
                context.bot.send_photo(chat_id=chat_id, photo=open(data, 'rb'), timeout=timeout)
        else:
            message(chat_id=chat_id, text=env['error'])

    
    if(env['service'] == 'alerts'):

        if(not env['service'] in [job.name for job in context.job_queue.jobs()]):

            status = 'Habilitado'
            queue['repeater'](callback=repeater, name=env['service'], interval=interval, context=update.message.chat_id)
        else:

            status = 'Desabilitado'
            context.job_queue.get_jobs_by_name(env['service'])[0].schedule_removal()

        message(chat_id=chat_id, text=(env['warning'] + status))
        
    else:
        queue['once'](callback=once, name=env['service'], context=update.message.chat_id, when=0)


    return None