from datetime import date

__DISPLAY = \
    '''
<div class="climate">
    <div class="local">
      <h1 style="color: white">{%CITY%}</h1>
      <img src="{%SRC%}" />
    </div>
    <div class="temperature">
      <h1 class="min">{%TEMP_MIN%}</h1>
      <h1 class="max">{%TEMP_MAX%}</h1>
    </div>
</div>
'''

__TITTLE = \
    '''
<div class="title">
  <h4 class="day">{%DAY%}</h4>
  <h4 class="date">{%DATE%}</h4>
</div>
'''

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

__MODEL_FILE = './app/view/model_weather.html'

def parser(data=[]):

    models = []
    model = open(__MODEL_FILE, 'r').read()

    for group in data:
        if(type(data) == list):
            climate = ''

            for d in group:
                climate += __DISPLAY.replace('{%CITY%}', d['city'].upper()) \
                    .replace('{%SRC%}', d['icon']) \
                    .replace('{%TEMP_MIN%}', d['min']) \
                    .replace('{%TEMP_MAX%}', d['max'])

            day = __DAYS[__TODAY.weekday()]
            month = __TODAY.strftime('%d/%m/%Y')

            tittle = __TITTLE.replace(
                '{%DAY%}', day).replace('{%DATE%}', month)

        models.append(
            model.replace('{%DISPLAY%}', climate)
            .replace('{%TITLE%}', tittle)
        )

    return models
