from .env import env

inmet, telegram, cptec, covid, alerts, paths, env \
= \
env['inmet'], env['telegram'], env['cptec'], env['covid'], env['alerts'], env['paths'], env

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