from app.controller.alerts.data import data
from app.controller.alerts.parser import parser
from app.controller.folder import folder
from glob import glob
import imgkit
import tempfile
import os

__OPTIONS_JPG = {
    'width': '745',
    'xvfb': ''
}

__NAME = 'alert'

def make():
    path = '{}/{}-*.jpg'.format(folder('Alerts'), __NAME)
    #files = glob(path)

    alerts = []

    messages = parser(data())

    for index, message in enumerate(messages):
        out = path.replace('*', str(index + 1))
        
        file = tempfile.NamedTemporaryFile(mode='w+', suffix='.html')        

        file.write(message['image'])

        imgkit.from_file(
            file.name,
            out,
            options=__OPTIONS_JPG
        )

        file.close()

        alerts.append({'file' : out, 'message' : message['text']})


    return alerts