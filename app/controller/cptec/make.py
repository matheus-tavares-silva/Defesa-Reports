from app.controller.cptec.data import data
from app.controller.cptec.parser import parser
from app.controller.folder import folder
import tempfile
import imgkit

__OUT_PATH = folder()
__OUT_NAME = 'cptec-*.jpg'
__OPTIONS_JPG = {
    'width': '1080',
    'height': '1920',
}

def make():

    html = parser(data())

    count = 1
    for page in html:
        file = tempfile.NamedTemporaryFile(mode='w+', suffix='.html')
        
        file.write(page)

        imgkit.from_file(
            file.name,
            (__OUT_PATH + '/' + __OUT_NAME).replace('*', str(count)),
            options=__OPTIONS_JPG
        )

        file.close()
        count += 1

    return True
