from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from lxml import etree, html, cssselect
from app import env
from datetime import datetime, timedelta, date

import os
import requests

os.environ['MOZ_HEADLESS'] = '1'  # -- Uncomment to show driver


def covid():
    driver = webdriver.Firefox(executable_path=env.gecko)

    wait = WebDriverWait(driver, 60)

    size = 10

    content = {'confirmed': '', 'interned': '',
               'recovered': '', 'isolated': '', 'dead': '', 'cities': [], 'cases': []}

    try:
        driver.get(env.covid['link'])

        driver.switch_to.frame(wait.until(
            EC.presence_of_element_located((By.XPATH, env.covid['path']['panel']))))

        for key in env.covid['path']:
            if(key in content.keys()):
                content[key] = wait.until(
                    EC.visibility_of_element_located(
                        (By.CSS_SELECTOR, env.covid['path'][key])
                    )
                ).text.replace(',', '.')

        button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, env.covid['path']['button'])
            )
        )

        ActionChains(driver).send_keys(
            Keys.PAGE_DOWN).click(button).pause(5).perform()

        for key in env.covid['path']['table']:
            buffer = []
            for i in range(size):
                element = wait.until(
                    EC.visibility_of_element_located(
                        (By.CSS_SELECTOR, env.covid['path']['table'][key].replace(
                            '%', str(i + 1)))
                    )
                )

                buffer.append(element.text.replace(',', '.'))

            content[key] = buffer

        monitored = str(int(content['interned'].replace(
            '.', '')) + int(content['isolated'].replace('.', '')))
        monitored = monitored[:2] + '.' + monitored[2:]
        del content['interned'], content['isolated']

        content.update({'monitored': monitored})
        content.update(
            {'date': (datetime.now() - timedelta(1)).strftime(u'%d/%m')})

    finally:
        try:
            driver.quit()
        except:
            pass

    return content        


def cptec(**kwargs):
    kwargs.update(kwargs if kwargs else env.cptec['default'])

    today = date.today()
    day = env.week_days[today.weekday()]
    month = today.strftime('%d/%m/%Y')

    geocodelist = [
        [
            str(
                requests.get(
                    env.cptec['api'] + 
                    env.cptec['route']['geocode'] + 
                    city, timeout=100
                ).json()[0]['geocode']
            ) for city in cities
        ] for cities in kwargs['cities']
    ]

    reponses = [
        {
            'day': day, 
            'month': month,
            'values' : 
            [   
                [ 
                    requests.get(
                        env.cptec['api'] + 
                        env.cptec['route']['prevision'] + 
                        code
                    ).json()[code][month]['tarde']
                ][0] for code in geocodes
            ] 
        } for geocodes in geocodelist
    ]

    return reponses

def alerts(**kwargs):
    kwargs.update(kwargs if kwargs else env.alerts['default'])

    def polygon(coordinates=[]):

        lines = [[round(float(b), 2) for b in a.split(' ')][::-1]
                 for a in coordinates.split(',')]

        lines[0].append(lines[-1][0])
        del lines[-1]
        lines.append(lines[0])

        return lines

    def search_for(country, xml):

        return country in [b.replace(' ', '', 1) if b[0] == ' ' else b for b in [a for a in xml.split(',')]]

    def response(link): 
        return {'url': link, 'source': html.fromstring(requests.get(link).content)}
    
    inmet = response(
        (env.alerts['link'] + kwargs['date'])) if kwargs['date'] else env.alerts['link'] + datetime.today().strftime('%Y/%m')

    if(not kwargs['date']):
        inmet = response('{}/{}'.format(inmet, [a.get('href')
                                                for a in response(inmet)['source'].xpath(env.alerts['path']['root'])][-1]))

    links = [[b, response(b)['source'].xpath(env.alerts['path']['root'])] for b in [
        inmet['url'] + a.get('href')[1:] for a in inmet['source'].xpath(env.alerts['path']['root'])][1:]][0]

    responses = [etree.XML(requests.get(
        links[0] + c.get('href')[2:]).content) for c in links[1][1:]]

    content = []
    format_date = lambda date : datetime.fromisoformat(date).strftime('%d/%m/%Y %H:%M')
    for xml in responses:
        position = 7 if xml[4].text in ['Update', 'Cancel'] else 6

        if(search_for(kwargs['country'], xml[position][19][1].text)):
            content.append(
                {
                    'type': xml[4].text,
                    'event': xml[position][2].text,
                    'onset': format_date(xml[position][7].text),
                    'expires': format_date(xml[position][8].text),
                    'headline': xml[position][10].text.split(':')[-1],
                    'description': xml[position][11].text,
                    'web': xml[position][13].text.split('/')[-1],
                    'color': xml[position][15][1].text,
                    'polygon': polygon(xml[position][20][1].text)
                }
            )

    return content