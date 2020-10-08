from app.controller.cptec import cptec
from app.controller.covid import covid
import threading

threads = [threading.Thread(target=cptec), threading.Thread(target=covid)]

def run(): 
    for thread in threads:
        thread.start()
    
    return None