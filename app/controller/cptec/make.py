from app.controller.cptec.data import data
from app.controller.cptec.parser import parser
from app.controller.folder import folder
import os
import tempfile
import imgkit

__OUT_FILES = [(folder() + '/' + 'cptec-*.jpg').replace('*', str((index + 1))) for index in range(2)]
__OPTIONS_JPG = {
    'width': '1080',
    'height': '1920',
}

def make():

    files = [True if os.path.exists(path) else False for path in __OUT_FILES ]
        
    if(False in files):
        html = parser(data())

        for index, page in enumerate(html):

            file = tempfile.NamedTemporaryFile(mode='w+', suffix='.html')

            file.write(page)

            imgkit.from_file(
                file.name,
                __OUT_FILES[index],
                options=__OPTIONS_JPG
            )

            file.close()        

    return __OUT_FILES
