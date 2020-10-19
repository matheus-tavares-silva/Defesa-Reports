from app.controller.alerts.data import data
from app.controller.alerts.save import save
from ..folder import folder
from .message import message

import imgkit
import tempfile
import os

__OPTIONS = {
    'xvfb': '',
    'width' : 1920,
    'height' : 1080
}

__NAME = 'alert'

def alerts():
    path = '{}/{}-*.png'.format(folder('Alerts'), __NAME)

    alerts = []

    contents = data()

    for content in contents:
        out = path.replace('*', content['web'])
        
        if(not os.path.isfile(out)):
            file = tempfile.NamedTemporaryFile(mode='w+', suffix='.html')        

            save(file, out, content)

            alerts.append({'file' : out, 'content' : message(content)})

    return alerts



if __name__ == "__main__":
    alerts()