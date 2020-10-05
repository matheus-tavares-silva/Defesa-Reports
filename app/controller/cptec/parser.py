from app.view.module import DISPLAY, TITTLE
from datetime import date

__DAYS = [
    'SEGUNDA-FEIRA',
    'TERÇA-FEIRA',
    'QUARTA-FEIRA',
    'QUINTA-FEIRA',
    'SEXTA-FEIRA',
    'SÁBADO',
    'DOMINGO'
]

__TODAY = date.today()

def html(data=[]):

    if(type(data) == list) :
        climate = ''

        for d in data:
            climate += DISPLAY.replace('{%CITY%}', d['city'].upper()) \
                .replace('{%SRC%}', d['icon']) \
                .replace('{%TEMP_MIN%}', d['min']) \
                .replace('{%TEMP_MAX%}', d['max'])
        

        day = __DAYS[__TODAY.weekday()]
        month = __TODAY.strftime('%d/%m/%Y')

        tittle = TITTLE.replace('{%DAY%}', day).replace('{%DATE%}', month)


    return {'display' : climate, 'tittle' : tittle}
