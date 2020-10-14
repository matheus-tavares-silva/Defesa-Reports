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

""" DATA = [
    [{'min': '26°', 'max': '41°', 'city': 'Cuiabá', 'icon': 'https://s1.cptec.inpe.br/webcptec/common/assets/images/icones/tempo/icones-grandes/pn.png'}, {'min': '19°', 'max': '35°', 'city': 'Juína', 'icon': 'https://s1.cptec.inpe.br/webcptec/common/assets/images/icones/tempo/icones-grandes/pp.png'}, {'min': '20°', 'max': '35°', 'city': 'Alta Floresta', 'icon': 'https://s1.cptec.inpe.br/webcptec/common/assets/images/icones/tempo/icones-grandes/pp.png'}, {'min': '20°', 'max': '40°', 'city': 'Vila Rica', 'icon': 'https://s1.cptec.inpe.br/webcptec/common/assets/images/icones/tempo/icones-grandes/pn.png'}, {'min': '20°', 'max': '41°', 'city': 'Barra do Garças', 'icon': 'https://s1.cptec.inpe.br/webcptec/common/assets/images/icones/tempo/icones-grandes/ps.png'}, {'min': '22°', 'max': '41°', 'city': 'Rondonópolis', 'icon': 'https://s1.cptec.inpe.br/webcptec/common/assets/images/icones/tempo/icones-grandes/pn.png'}],
    [{'min': '24°', 'max': '40°', 'city': 'Cáceres', 'icon': 'https://s1.cptec.inpe.br/webcptec/common/assets/images/icones/tempo/icones-grandes/pn.png'}, {'min': '23°', 'max': '38°', 'city': 'Tangará da Serra', 'icon': 'https://s1.cptec.inpe.br/webcptec/common/assets/images/icones/tempo/icones-grandes/pn.png'}, {'min': '23°', 'max': '41°', 'city': 'Diamantino', 'icon': 'https://s1.cptec.inpe.br/webcptec/common/assets/images/icones/tempo/icones-grandes/pn.png'}, {'min': '18°', 'max': '39°', 'city': 'Sorriso', 'icon': 'https://s1.cptec.inpe.br/webcptec/common/assets/images/icones/tempo/icones-grandes/pn.png'}, {'min': '20°', 'max': '36°', 'city': 'Juara', 'icon': 'https://s1.cptec.inpe.br/webcptec/common/assets/images/icones/tempo/icones-grandes/pp.png'}, {'min': '18°', 'max': '38°', 'city': 'Sinop', 'icon': 'https://s1.cptec.inpe.br/webcptec/common/assets/images/icones/tempo/icones-grandes/pn.png'}]
]
 """
 
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

            tittle = __TITTLE.replace('{%DAY%}', day).replace('{%DATE%}', month)

        models.append(
            model.replace('{%DISPLAY%}',climate) \
                .replace('{%TITLE%}', tittle)
        )
    
    
    
    return models