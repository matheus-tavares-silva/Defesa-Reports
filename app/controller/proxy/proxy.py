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

from .render  import Render

os.environ['MOZ_HEADLESS'] = '1'  # -- Uncomment to show driver
class Proxy(Render):
    def __init__(self):
        pass

    @staticmethod
    def covid(**kwargs):
        driver = webdriver.Firefox(executable_path=env.gecko)

        wait = WebDriverWait(driver, 120)

        size = 10

        content = {'confirmed': '', 'interned': '',
                'recovered': '', 'isolated': '', 'dead': '', 'cities': [], 'cases': []}

        try:
            driver.get(env.covid['link'])
            per1, per2 = False, False

            if(per1): # Habilitar/Desabilitar caso o layout da pag mude
                next_page = wait.until(
                    EC.element_to_be_clickable(
                        (By.XPATH, env.covid['path']['next'])
                    )
                )

                next_page.click()

            for key in env.covid['path']:
                if(key in content.keys()):
                    content[key] = wait.until(
                        EC.visibility_of_element_located(
                            (By.CSS_SELECTOR, env.covid['path'][key])
                        )
                    ).text.replace(',', '.')

            if(per2): # Habilitar/Desabilitar caso o layout da pag mude
                button = wait.until(
                    EC.element_to_be_clickable(
                        (By.XPATH, env.covid['path']['button'])
                    )
                )

                button.click()

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

            monitored = str(
                int(content['interned'].replace('.', '').replace(',', '')) + 
                int(content['isolated'].replace('.', ',').replace(',', ''))
            )

            if(len(monitored) > 3):
                dot = len(monitored) - 3
                monitored = monitored[:dot] + '.' + monitored[dot:]

            del content['interned'], content['isolated']

            content.update({'monitored': monitored})
            content.update({'date': (datetime.now() - timedelta(1)).strftime(u'%d/%m')})
        except:
            content = None
        finally:
            try:
                driver.quit()
            except:
                pass

        return Render(content, 'covid').content if content else content

    @staticmethod
    def cptec(**kwargs):
        kwargs.update(kwargs if kwargs else env.cptec['default'])

        today = date.today()
        day = env.week_days[today.weekday()]
        month = today.strftime('%d/%m/%Y')

        try:
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
        except:
            return None

        return Render(reponses, 'cptec').content

    @staticmethod
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
        
        try:
            data = response(
                (env.alerts['link'] + kwargs['date'])) if kwargs['date'] else env.alerts['link'] + datetime.today().strftime('%Y/%m')

            if(not kwargs['date']):
                data = response('{}/{}'.format(data, [a.get('href')
                                                        for a in response(data)['source'].xpath(env.alerts['path']['root'])][-1]))

            links = [[b, response(b)['source'].xpath(env.alerts['path']['root'])] for b in [
                data['url'] + a.get('href')[1:] for a in data['source'].xpath(env.alerts['path']['root'])][1:]][0]

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
        except:
            return None

        return Render(content, 'alerts').content

    @staticmethod
    def inmet(**kwargs):
        station     = env.inmet['stations'][kwargs.get('city', 'CUIABÁ').upper()]
        date_start  = kwargs.get('date_start', datetime.today().strftime('%Y-%m-%d'))
        date_end    = kwargs.get('date_end', datetime.today().strftime('%Y-%m-%d'))
        hour_start  = kwargs.get('hour_start', '00:00').replace(':', '') 
        hour_end    = kwargs.get('hour_end', '23:00').replace(':', '')
        filter_by   = kwargs.get('filter_by', ['CHUVA', 'VENTO'])
        enable_temp = kwargs.get('enable_temp', True)

        try:
            reponse = requests.get(
                env.inmet['api'] + 
                env.inmet['route']['station'] +
                '{}/{}/{}'.format(date_start, date_end, station)
            ).json()
        except:
            return None

        if(reponse):
            data = {
                'station'     : station,
                'display'     : filter_by,
                'temperature' : enable_temp,
                'values'  : [
                    {
                        'date' : content['DT_MEDICAO'] or '',
                        'hour' : content['HR_MEDICAO'][:2] + ':' + content['HR_MEDICAO'][2:]   if content['DT_MEDICAO'] != ''             else '',
                        'temp_inst': round(float(content['TEM_INS']), 2)        if content['TEM_INS'] != None  and enable_temp            else '',
                        'temp_min' : round(float(content['TEM_MIN']), 2)        if content['TEM_MIN'] != None  and enable_temp            else '',
                        'temp_max' : round(float(content['TEM_MAX']), 2)        if content['TEM_MAX'] != None  and enable_temp            else '',
                        'wind_vel' : round(float(content['VEN_VEL']) * 3.6, 2)  if content['VEN_VEL'] != None  and 'VENTO' in filter_by   else '',
                        'wind_dir' : round(float(content['VEN_DIR']), 2)        if content['VEN_DIR'] != None  and 'VENTO' in filter_by   else '',
                        'wind_raj' : round(float(content['VEN_RAJ']) * 3.6, 2)  if content['VEN_RAJ'] != None  and 'VENTO' in filter_by   else '',
                        'rain_mm'  : round(float(content['CHUVA'])  , 2)        if content['CHUVA']   != None  and 'CHUVA' in filter_by   else '',
                    } for content in reponse if int(content['HR_MEDICAO']) >= int(hour_start) and int(content['HR_MEDICAO']) <= int(hour_end) 
                ]
            }
        else:
            return None

        return Render(data, 'inmet').content
    
    