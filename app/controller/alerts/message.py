from datetime import datetime

__STATE = {
    'Cancel': 'Cancelado ' + '❌',
    'Update': 'Atualizado ' + '❗',
    'Alert': 'Ativo ' + '✔'
}

__MAIN_TEXT = \
"""
Situação: <b>{}</b>
Aviso: <b>{}</b>
{}

{}

http://alert-as.inmet.gov.br/cv/emergencia/cap/{}
"""

__TIME_TEXT = \
"""
Início: {}
Término: {}
"""


def message(content):

    text = __MAIN_TEXT.format(
        __STATE[content['type']],
        content['event'],
        content['headline'].split('.')[1],
        __format_status(content['type'], content['description'], [
                            content['onset'], content['expires']]),
        content['web']
    )

    return text


def __format_status(status, description, date):

    if(status == 'Cancel'):
        description = [string.replace(' ', '', 1) if string[0] == ' ' else string for string in description.split(
            '.')[0:2]]

        description = description[0] + '\n' + description[1]
    else:
        duration = \
        __TIME_TEXT.format(__format_date(date[0]), __format_date(date[1]))

        description = duration + description

    return description


def __format_date(date):
    return datetime.fromisoformat(date).strftime('%d/%m/%Y %H:%M')
