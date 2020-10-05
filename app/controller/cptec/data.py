from lxml import etree, html
import requests

__LINK = 'https://www.cptec.inpe.br/previsao-tempo/mt/'

__XPATH_TEMP = {'min': '/html/body/div[2]/div[5]/div[1]/div/div[2]/div[4]/div[1]/span',
                'max': '/html/body/div[2]/div[5]/div[1]/div/div[2]/div[4]/div[2]/span',
                'city': '/html/body/div[2]/div[5]/div[1]/div/h2',
                'icon': '/html/body/div[2]/div[5]/div[1]/div/div[2]/div[2]/a/img/@src'}


def temperature(city=['cuiaba']):
    value = []

    if(type(city) is list):
        for c in city:
            try:
                response = html.fromstring(requests.get(__LINK + c).content)
            except:
                pass
            else:
                model = {'min': '', 'max': '', 'city': '', 'icon': ''}
                for data in __XPATH_TEMP:
                    if(data == 'icon'):
                        model[data] = response.xpath(__XPATH_TEMP[data])[0]
                    else:
                        model[data] = response.xpath(__XPATH_TEMP[data])[0].text_content().replace(u'\xa0', u'').replace('/MT', '')

            value.append(model)

        return value
    
    return None