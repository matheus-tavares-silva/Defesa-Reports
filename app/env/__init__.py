from .env import env

report_2, covid_2, cptec_2, local_report, report, inmet, telegram, cptec, covid, alerts, paths, env \
= \
env['report_2'], env['covid_2'], env['cptec_2'], env['local_report'], env['report'], env['inmet'], env['telegram'], env['cptec'], env['covid'], env['alerts'], env['paths'], env

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