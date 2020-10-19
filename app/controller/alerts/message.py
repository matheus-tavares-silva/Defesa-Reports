from datetime import datetime

def message(content):

    
    onset = datetime.fromisoformat(content['onset']).strftime('%d/%m/%Y %H:%M')
    expires = datetime.fromisoformat(content['expires']).strftime('%d/%m/%Y %H:%M')

    formated = \
    str(
        """
        Aviso de {}
        {}

        Início: {}
        Término: {}

        {}

        http://alert-as.inmet.gov.br/cv/emergencia/cap/{}
        """
    ).format(content['event'], content['headline'].split('.')[1], onset, expires, content['description'], content['description'], content['web'])

    return formated