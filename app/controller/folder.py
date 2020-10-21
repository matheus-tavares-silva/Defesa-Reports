import os
from datetime import date, datetime

__DEFAULT_FOLDER = './out'


def folder(folder=None, sigle=True):
    today = '/' + datetime.today().strftime('%d-%m-%Y')
    today_folder = __DEFAULT_FOLDER + today

    if(not os.path.exists(__DEFAULT_FOLDER)):
        os.mkdir(__DEFAULT_FOLDER, 0o777)
    if(not os.path.exists(today_folder)):
        os.mkdir(today_folder, 0o777)
    if(folder):
        custom = today_folder + '/' + folder if sigle else __DEFAULT_FOLDER + '/' + folder

        if(not os.path.exists(custom)):
            os.mkdir(custom, 0o777)

        return custom

    return today_folder


if __name__ == "__main__":
    folder()
