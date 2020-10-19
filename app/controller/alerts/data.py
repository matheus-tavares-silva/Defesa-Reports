import requests
from lxml import etree, html
from datetime import datetime

__BASE = 'https://alerts.inmet.gov.br/cap_12/'

__XPATH = {
    'root' : '/html/body/table/tr/td/a'
}

def data(country='Mato Grosso', date=None):

    response = lambda link: {'url' : link, 'source' : html.fromstring(requests.get(link).content)}

    inmet = response((__BASE + date)) if date else __BASE + datetime.today().strftime('%Y/%m')

    if(not date):
        inmet = response('{}/{}'.format(inmet, [a.get('href') for a in response(inmet)['source'].xpath(__XPATH['root'])][-1]))
    
    links = [[b, response(b)['source'].xpath(__XPATH['root'])] for b in [inmet['url'] + a.get('href')[1:] for a in inmet['source'].xpath(__XPATH['root'])][1:]][0]

    responses = [etree.XML(requests.get(links[0] + c.get('href')[2:]).content) for c in links[1][1:]]

    content = []
    for xml in responses:
        position = 6 if xml[4].text != 'Update' else 7

        if(search_for(country, xml[position][19][1].text)):
            content.append(
                {
                    'event' : xml[position][2].text,
                    'onset' : xml[position][7].text,
                    'expires' : xml[position][8].text,
                    'headline' : xml[position][10].text,
                    'description' : xml[position][11].text,
                    'web' : xml[position][13].text.split('/')[-1],
                    'color' : xml[position][15][1].text,
                    'polygon' : polygon(xml[position][20][1].text)
                }
            )

    return content

def polygon(coordinates=[]):

    lines = [[round(float(b), 2) for b in a.split(' ')][::-1] for a in coordinates.split(',')]

    lines[0].append(lines[-1][0])
    del lines[-1]
    lines.append(lines[0])

    return lines

def search_for(country, xml):

    return country in [ b.replace(' ', '', 1) if b[0] == ' ' else b for b in [a for a in xml.split(',')]]
