from app.controller.cptec.make import make as cptec
from app.controller.covid.make import make as covid
from app.controller.alerts import alerts
from app.controller.bot.chat import chat


def run(): 
    #alerts()
    #covid()
    #cptec()
    chat()
    
    return None
    