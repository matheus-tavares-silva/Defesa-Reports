from app.controller.covid.data import data
from app.controller.covid.parser import parser
import tempfile
import imgkit

__OUT_HTML_FILE = 'out/covid.html'
__OUT_HTML_JPG = 'out/covid-*.jpg'

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

    info = parser(data())

    count = 1
    for html in info:
        file = tempfile.NamedTemporaryFile(mode='w+', suffix='.html')
        
        file.write(html)

        imgkit.from_file(
            file.name,
            __OUT_HTML_JPG.replace('*', str(count)),
            options=__OPTIONS_JPG[count - 1]
        )

        file.close()
        count += 1

    return None
