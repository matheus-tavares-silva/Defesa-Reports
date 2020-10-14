from app.controller.cptec.data import data
from app.controller.cptec.parser import parser
from app.controller.folder import folder
from glob import glob
import os
import tempfile
import imgkit

__OPTIONS_JPG = {
    'width': '1080',
    'height': '1920',
    'xvfb': ''
}

__NAME = 'cptec'

def make():
    path = '{}/{}-*.jpg'.format(folder(), __NAME)
    files = glob(path)

    alerts = []

    if(not files):
        html = parser(data())

        for index, page in enumerate(html):
            out = path.replace('*', str(index + 1))
             
            file = tempfile.NamedTemporaryFile(mode='w+', suffix='.html')

            file.write(page)
            
            imgkit.from_file(
                file.name,
                out,
                options=__OPTIONS_JPG
            )

            file.close()

            alerts.append({'file' : out, 'message' : None})
    else:
        alerts = [{'file' : name, 'message' : None} for name in files]

    return alerts