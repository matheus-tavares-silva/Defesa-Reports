from datetime import datetime, timedelta

__YESTERDAY = datetime.now() - timedelta(1)

__MODEL_FILES = ['./app/view/model_insta_corona.html', './app/view/model_corona.html']


def parser(data=[]):

    models = []
    for f in __MODEL_FILES:
        model = open(f, 'r').read()

        rank = ''
        if(len(data['cities']) == len(data['cases'])):
            for i in range(len(data['cities'])):
                if(i <= 7):
                    rank += ' {0} ({1}),'.format(data['cities']
                                                [i], data['cases'][i])
                elif(i == 8):
                    rank += ' {0} ({1}) e'.format(data['cities']
                                                [i], data['cases'][i])
                elif(i == 9):
                    rank += ' {0} ({1}).'.format(data['cities']
                                                [i], data['cases'][i])

        monitored = str(int(data['interned'].replace(
            '.', '')) + int(data['isolated'].replace('.', '')))
        monitored = monitored[:2] + '.' + monitored[2:]

        models.append(
            model.replace('{%DATE%}', __YESTERDAY.strftime(u'%d/%m')) \
                .replace('{%CONFIRMED%}', data['confirmed']) \
                .replace('{%RECOVERED%}', data['recovered']) \
                .replace('{%MONITORED%}', monitored) \
                .replace('{%DEAD%}', data['dead']) \
                .replace('{%LIST%}', rank)
        )
    
    return models