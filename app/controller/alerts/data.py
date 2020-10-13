from lxml import etree, html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import os

__LINK = 'http://alert-as.inmet.gov.br/cv/'

__GECKO = 'app/controller/covid/geckodriver'

__SELECTORS = {
    'country' : 'div.cinza2:nth-child(2) > div:nth-child(3) > a',
}

__SITUATION = {
    'severity' : '#severity',
    'event' : '#event',
    'onset' : '#onset',
    'expires' : '#expires',
    'description' : '#description',
    'map' : r'#OpenLayers\.Map_3_OpenLayers_ViewPort'
}


def data() :
    os.environ['MOZ_HEADLESS'] = '1' #-- Uncomment to show driver

    response = html.fromstring(requests.get(__LINK).content)

    driver = webdriver.Firefox(executable_path=__GECKO)
    wait = WebDriverWait(driver, 40)

    elements = response.cssselect(__SELECTORS['country'])

    situation = []
    for element in elements:
        aux = {}
        driver.get(element.get('href'))
        for key in __SITUATION:
            if(not key == 'map'):
                aux[key] =  wait.until(
                    EC.visibility_of_element_located(
                        (By.CSS_SELECTOR, __SITUATION[key])
                    )
                ).text
            else:
                aux['map'] = wait.until(
                    EC.visibility_of_element_located(
                        (By.CSS_SELECTOR, __SITUATION[key])
                    )
                ).get_attribute('innerHTML').replace('visibility: hidden;', 'visibility: inherit;').replace('opacity: 0;', 'opacity: 1;')
                
        situation.append(aux)

    driver.close()

    return situation