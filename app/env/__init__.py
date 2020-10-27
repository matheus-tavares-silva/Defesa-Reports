from .env import env

cptec, covid, alerts, env \
= \
env['cptec'], env['covid'], env['alerts'], env

gecko = './geckodriver'

week_days = [
    'SEGUNDA-FEIRA',
    'TERÇA-FEIRA',
    'QUARTA-FEIRA',
    'QUINTA-FEIRA',
    'SEXTA-FEIRA',
    'SÁBADO',
    'DOMINGO'
]