from app.controller.covid.data import panel
from app.controller.covid.parser import html
import imgkit

__OUT_HTML_FILE = 'out/insta_covid.html'
__OUT_HTML_JPG = 'out/insta_covid.jpg'
__OPTIONS_JPG = {
    'width': '1080',
    'height': '1920',
}


def covid():

    info = html(panel())

    with open(__OUT_HTML_FILE, 'w+') as file:
        file.write(info)

    imgkit.from_file(
        __OUT_HTML_FILE,
        __OUT_HTML_JPG,
        options=__OPTIONS_JPG
    )

    return None