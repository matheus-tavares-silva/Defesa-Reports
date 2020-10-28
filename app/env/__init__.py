from .env import env

paths, telegram, cptec, covid, alerts, env \
= \
env['paths'], env['telegram'], env['cptec'], env['covid'], env['alerts'], env

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