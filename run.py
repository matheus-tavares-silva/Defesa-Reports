import data
import parser

model = open('view/model.html', 'r').read()

data = parser.html(data.temperature(['cuiaba', 'juina', 'rondonopolis', 'sorriso', 'sinop']))

with open('test.html', 'w+') as file :
    file.write(model.replace('{%DISPLAY%}', data['display']).replace('{%TITLE%}', data['tittle']))
