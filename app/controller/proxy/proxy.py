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
        only_content = kwargs.get('only_content', False)
        city         = kwargs.get('city', '')

        driver = webdriver.Firefox(executable_path=env.gecko)

        wait = WebDriverWait(driver, 120)

        size = 10

        content = {
            'confirmed': '', 
            'interned': '',
            'recovered': '', 
            'isolated': '', 
            'dead': '', 
            'cities': [], 
            'cases': []
        }

        try:
            driver.get(env.covid['link'])
            next_page, back_page, order = False, True, False

            if(next_page): # Habilitar/Desabilitar caso o layout da pag mude
                next_page = wait.until(
                    EC.element_to_be_clickable(
                        (By.XPATH, env.covid['path']['next'])
                    )
                )

                next_page.click()
            elif(back_page):
                next_page = wait.until(
                    EC.element_to_be_clickable(
                        (By.XPATH, env.covid['path']['back'])
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

            if(order): # Habilitar/Desabilitar caso o layout da pag mude
                button = wait.until(
                    EC.element_to_be_clickable(
                        (By.XPATH, env.covid['path']['button'])
                    )
                )

                button.click()

            if(city != ''):
               print('hello')

            else:
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
        
        return Render(content, 'covid').content if not only_content and content else content
        
    @staticmethod
    def cptec(**kwargs):
        search_cities = kwargs.get('search_cities', env.cptec['default']['cities'])
        only_data     = kwargs.get('only_data', False)
        format_data   = kwargs.get('format_data', False)

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
                ] for cities in search_cities
            ]

            if(only_data):
              reponses = [
                    [   
                        [ 
                            requests.get(
                                env.cptec['api'] + 
                                env.cptec['route']['prevision'] + 
                                code
                            ).json()[code]
                        ][0] for code in geocodes
                    ] for geocodes in geocodelist
                ]

            else:
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
            return []

        if(format_data or only_data):
            return reponses

        return Render(reponses, 'cptec').content

    @staticmethod
    def alerts(**kwargs):
        import operator

        format_date  = lambda date : datetime.fromisoformat(date).strftime('%d/%m/%Y %H:%M')
        response     = lambda link : {'url': link, 'source': html.fromstring(requests.get(link).content)}
        compare_date = lambda date : datetime.strptime(date, '%d/%m/%Y %H:%M') > datetime.now()
        search_for   = lambda contry, xml : country in [b.replace(' ', '', 1) if b[0] == ' ' else b for b in [a for a in xml.split(',')]]

        country     = kwargs.get('country', 'Mato Grosso')
        alert_dates = kwargs.get('date', [datetime.today().strftime('%Y/%m/%d')])
        to_report   = kwargs.get('to_report', False)

        def polygon(coordinates=[]):

            lines = [[round(float(b), 2) for b in a.split(' ')][::-1]
                    for a in coordinates.split(',')]

            lines[0].append(lines[-1][0])
            del lines[-1]
            lines.append(lines[0])

            return lines
        
        contents = []
        for alert_date in alert_dates:
            try:
                data = response(env.alerts['link'] + alert_date)

                if(not alert_date):
                    data = response('{}/{}'.format(data, [a.get('href')
                                                            for a in response(data)['source'].xpath(env.alerts['path']['root'])][-1]))

                links = [
                    [b, response(b)['source'].xpath(env.alerts['path']['root'])] for b in [
                        data['url'] + a.get('href')[1:] for a in data['source'].xpath(env.alerts['path']['root'])
                    ][1:]
                ][0]

                responses = [etree.XML(requests.get(links[0] + c.get('href')[2:]).content) for c in links[1][1:]]
                
                for xml in responses:
                    position = 7 if xml[4].text in ['Update', 'Cancel'] else 6

                    if(search_for(country, xml[position][19][1].text)):
                        contents.append(
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
                pass
        
        if(to_report):
            contents = list(filter(lambda content : compare_date(content['expires']) and content['type'] != 'Cancel', contents))

        return Render(contents, 'alerts', overwrite=to_report).content

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

    @staticmethod
    def report(**kwargs):

        from ...models.db import read, write
        fire_sum    = lambda r : sum(list(map(lambda e: int(e.split(',')[1]) if e != '' else 0, r)))
        get_abspath = lambda f : os.path.abspath(f)
        today       = datetime.today().strftime('%d/%m/%Y')

        filters = {
            'date_start' : kwargs.get('date_start', (datetime.now() - timedelta(1)).strftime('%Y-%m-%d 00:00:00')),
            'date_end'   : kwargs.get('date_end', datetime.now().strftime('%Y-%m-%d 23:59:59')),
            'date_range' : [datetime.now().strftime('%Y/%m/%d'),(datetime.now() - timedelta(1)).strftime('%Y/%m/%d')]
        }

        icons = {
            'Acumulo de Chuva' : get_abspath('app/view/static/icon/icon_acumulo-chuva.png'),
            'Onda de Calor'    : get_abspath('app/view/static/icon/icon_onda-calor.png'),
            'Chuvas Intensas'  : get_abspath('app/view/static/icon/icon_chuvas-intensas.png'),
        }

        json_data = read()
        if(json_data['report']['updated'] != today):
            json_data['report'].update(
                {
                    'updated' : today,
                    'number'  : json_data['report']['number'] + 1,
                    'panel'  : json_data['report']['panel'] + 1
                }
            )
            write('report', json_data)

        response = requests.get(env.report['api']['foco'].format(filters['date_start'], filters['date_end'])).text.split('\n')[1:]
        content = {
            'today'      : today,
            'number'     : str(json_data['report']['number']),
            'panel'      : str(json_data['report']['panel']),
            'covid'      : Proxy.covid(only_content=True),
            'alerts'     : Proxy.alerts(date=filters['date_range'], to_report=True),
            'fires_acul' : fire_sum(response),
            'icons'      : icons,
            'fires'      :  [
                {
                    'city'      : element[0].replace('(MATO GROSSO)', ''),
                    'fires'     : int(element[1]),
                } for index, element in enumerate([content.split(',') for content in response if content != '']) if index <= 10
            ]
        }

        return Render(content, 'report', method='selenium', use_temp=True, page_size={'width' : 1080, 'height' : 1995}, folium_zoom=8).content
    
    @staticmethod
    def local_report(**kwargs):
        city        = kwargs.get('city', 'Poconé')
        format_date = lambda input_date : input_date.strftime('%d/%m/%Y')  
        
        covid_content = requests.post(env.local_report['api'], data=env.local_report['payload']).json()
        cptec_content = Proxy.cptec(search_cities=[[city]], only_data=True)
    
        if(covid_content and cptec_content):
            today    = format_date(date.today())
            tomorrow = format_date(date.today() + timedelta(days=1))

            covid_data = [{
                'Município'     : data['Filtros aplicados:\nCodigoIBGE não é 0000000 Municípios'].upper() if data['Filtros aplicados:\nCodigoIBGE não é 0000000 Municípios'] else 'N/A',
                'Confirmado'    : data['Confirmados']           if data['Confirmados'] else 'N/A' ,
                'Monitorado'    : data['Em Monitoramento']      if data['Em Monitoramento'] else 'N/A',
                'Óbitos'        : data['Óbitos']                if data['Óbitos'] else 'N/A',
                'Incidência'    : round(data['Incidência'],  1) if data['Incidência'] else 'N/A',
                'Mortalidade'   : round(data['Mortalidade'], 1) if data['Mortalidade'] else 'N/A'
            } for data in covid_content['data'] if list(data.items())[0][1] == city][0]

            content = {
                'today' : today[0:5],
                'tomorrow' : tomorrow[0:5],
                'covid' : covid_data,
                'cptec' : {
                    'today'     : cptec_content[0][0][today]['tarde'],
                    'tomorrow'  : cptec_content[0][0][tomorrow]['tarde']
                }
            }

            return Render(content, 'local_report').content
        
        return None
    
    @staticmethod
    def cptec_2(**kwargs):
        from ...models.db import read, write
        
        today = datetime.today().strftime('%d/%m/%Y')

        json_data = read()
        if(json_data['report']['updated'] != today):
            json_data['report'].update(
                {
                    'updated' : today,
                    'number'  : json_data['report']['number'] + 1,
                    'panel'  : json_data['report']['panel'] + 1
                }
            )
            write('report', json_data)

        content = []
        for data in Proxy.cptec(format_data=True):
            content.append({
                'cptec'     : data,
                'date'      : today,
                'number'    : str(json_data['report']['number']),
            })

        
        return Render(content, 'cptec_2').content
    
    @staticmethod
    def covid_2(**kwargs):
        from ...models.db import read, write
        
        today = datetime.today().strftime('%d/%m/%Y')

        json_data = read()
        if(json_data['report']['updated'] != today):
            json_data['report'].update(
                {
                    'updated' : today,
                    'number'  : json_data['report']['number'] + 1,
                    'panel'  : json_data['report']['panel'] + 1
                }
            )
            write('report', json_data)
        
        content = {
            'covid'     : Proxy.covid(only_content=True),
            'date'      : today,
            'number'    : str(json_data['report']['number']),
        }

        return Render(content, 'covid_2').content
    
    @staticmethod
    def report_2(**kwargs):
        from ...models.db import read, write

        filters = {
            'date_start' : kwargs.get('date_start', (datetime.now() - timedelta(1)).strftime('%Y-%m-%d 00:00:00')),
            'date_end'   : kwargs.get('date_end', datetime.now().strftime('%Y-%m-%d 23:59:59')),
            'date_range' : [datetime.now().strftime('%Y/%m/%d'),(datetime.now() - timedelta(1)).strftime('%Y/%m/%d')]
        }
        
        today = datetime.today().strftime('%d/%m/%Y')

        json_data = read()
        if(json_data['report']['updated'] != today):
            json_data['report'].update(
                {
                    'updated' : today,
                    'number'  : json_data['report']['number'] + 1,
                    'panel'  : json_data['report']['panel'] + 1
                }
            )
            write('report', json_data)

        content = []
        for report in Proxy.alerts(date=filters['date_range'], to_report=True):
            content.append({
                'alerts'    : report,
                'date'      : today,
                'number'    : str(json_data['report']['number']),
            })

        return Render(content, 'report_2').content