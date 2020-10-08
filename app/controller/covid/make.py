from app.controller.covid.data import data
from app.controller.covid.parser import parser
from app.controller.folder import folder
import tempfile
import imgkit

__OUT_PATH = folder()
__OUT_NAME = 'covid-*.jpg'
__OPTIONS_JPG = [
    {
        'width': '1080',
        'height': '1920',
    },
    {
        'width': '1080',
        'height': '1080',
    }
]


def make():

    html = parser(data())

    count = 1
    for page in html:
        file = tempfile.NamedTemporaryFile(mode='w+', suffix='.html')
        
        file.write(page)

        imgkit.from_file(
            file.name,
            (__OUT_PATH + '/' + __OUT_NAME).replace('*', str(count)),
            options=__OPTIONS_JPG[count - 1]
        )

        file.close()
        count += 1

    return None
