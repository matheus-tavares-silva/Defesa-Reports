from app.controller.cptec.make import make as cptec
from app.controller.covid.make import make as covid
from app.controller.bot.chat import chat
import threading

#threads = [threading.Thread(target=cptec), threading.Thread(target=covid)]

def run(): 
    chat()
    #for thread in threads:
    #    thread.start() 
    
    return None
    