import os
from datetime import date, datetime
from ..env import paths



def folder(folder=None, sigle=True):
    dayfolder = paths['out'] + datetime.today().strftime('%d-%m-%Y')

    if(not os.path.exists(paths['out'])):
        os.mkdir(paths['out'], 0o777)
    if(not os.path.exists(dayfolder)):
        os.mkdir(dayfolder, 0o777)
    if(folder):
        custom = dayfolder + '/' + folder if sigle else paths['out'] + folder

        if(not os.path.exists(custom)):
            os.mkdir(custom, 0o777)

        return custom

    return dayfolder + '/'


if __name__ == "__main__":
    folder()
