from datetime import date

__DEFAULT = \
'''
Aviso de: {}
Grau de severidade: {}

Início: {}
Fim: {}

{}
'''

def parser(data=[]):

    infos = []
    for item in data:
        aux = {
            'image' : item['map'],
            'text' : __DEFAULT.format(item['event'], item['severity'], item['onset'], item['expires'], item['description'])
        }

        infos.append(aux)

    return infos