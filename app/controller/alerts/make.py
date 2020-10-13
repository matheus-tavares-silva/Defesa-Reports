from app.controller.alerts.data import data
from app.controller.alerts.parser import parser
from app.controller.folder import folder
import imgkit
import tempfile
import os

__OUT_FILES = [(folder('Alerts') + '/' + 'alerts-*.jpg').replace('*', str((index + 1))) for index in range(2)]

__OPTIONS_JPG = {
    'width': '745',
    'xvfb': ''
}

def make():

    files = [True if os.path.exists(path) else False for path in __OUT_FILES ]

    alerts = []

    if(False in files):
        messages = parser(data())
        for index, message in enumerate(messages):
            out_file = __OUT_FILES[index]
            
            file = tempfile.NamedTemporaryFile(mode='w+', suffix='.html')        

            file.write(message['image'])

            imgkit.from_file(
                file.name,
                out_file,
                options=__OPTIONS_JPG
            )

            file.close()

            alerts.append({'file' : out_file, 'message' : message['text']})

    return alerts