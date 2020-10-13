from lxml import etree, html
import requests

__LINK = 'https://www.cptec.inpe.br/previsao-tempo/mt/'

__XPATH_TEMP = {'min': '/html/body/div[2]/div[5]/div[1]/div/div[2]/div[4]/div[1]/span',
                'max': '/html/body/div[2]/div[5]/div[1]/div/div[2]/div[4]/div[2]/span',
                'city': '/html/body/div[2]/div[5]/div[1]/div/h2',
                'icon': '/html/body/div[2]/div[5]/div[1]/div/div[2]/div[2]/a/img/@src'}

__DEFAULT_CITIES = citie_group=[['cuiaba', 'juina', 'alta_floresta', 'vila_rica', 'barra_do_garcas', 'rondonopolis'], ['caceres', 'tangara_da_serra', 'diamantino', 'sorriso', 'juara', 'sinop']]

def data(cities=__DEFAULT_CITIES):

    if(type(cities) is list):
        total = []
        for group in cities:
            values = []
            for city in group:
                try:
                    response = html.fromstring(requests.get(__LINK + city).content)
                except:
                    pass
                else:
                    model = {'min': '', 'max': '', 'city': '', 'icon': ''}

                    for path in __XPATH_TEMP:

                        if(path == 'icon'):
                            model[path] = response.xpath(__XPATH_TEMP[path])[0]
                        else:
                            model[path] = response.xpath(__XPATH_TEMP[path])[0].text_content().replace(u'\xa0', u'').replace('/MT', '')
                    
                values.append(model)
            total.append(values)

        return total
    
    return None