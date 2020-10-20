from .message import message
from selenium import webdriver
from concurrent.futures import ThreadPoolExecutor as executor
from time import sleep 

import tempfile
import os
import folium

__CENTER = [-12.38, -54.92]

__GECKO = './geckodriver'


def __map(out, content):
    
    file = tempfile.NamedTemporaryFile(mode='w+', suffix='.html')

    os.environ['MOZ_HEADLESS'] = '1'  # -- Uncomment to show driver

    if(__build(file.name, content)):

        driver = webdriver.Firefox(executable_path=__GECKO)

        # print(file.name)
        driver.set_window_size(1920, 1080)

        driver.get('file:///' + file.name)

        sleep(10)

        driver.save_screenshot(out)

        driver.close()

    file.close()

    return {'file': out, 'message': message(content)}


def __build(file, data=[]):

    try:
        city = folium.Map(location=__CENTER, zoom_start=6)

        polygon = data['polygon']

        folium.Polygon(polygon,  color=data['color'], fill=True,
                       fillColor=data['color'], fillOpacity=1).add_to(city)

        city.save(file)
    except:
        return False

    return True


def save(out, content):

    future = executor().submit(__map, out, content)

    return future
