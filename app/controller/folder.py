import os
from datetime import date, datetime

__DEFAULT_FOLDER = 'Boletim'

def folder(path='/home/s0berano/Documents'):
    location = path + '/' + __DEFAULT_FOLDER
    today = '/' + datetime.today().strftime('%d-%m-%Y')
    today_folder = location + today

    if(os.path.exists(path)):
        if(not os.path.exists(location)):
            os.mkdir(location, 0o777)
        if(not os.path.exists(today_folder)):
            os.mkdir(today_folder, 0o777)

    else:
        return False

    return today_folder

if __name__ == "__main__":
    folder()
