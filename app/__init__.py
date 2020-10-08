from app.controller.cptec import cptec
from app.controller.covid import covid
import threading

cptec = threading.Thread(target=cptec)
covid = threading.Thread(target=covid)

def run(): 
    cptec.start()
    covid.start()