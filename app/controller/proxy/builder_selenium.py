from selenium import webdriver
from selenium.common.exceptions import InvalidSessionIdException
from concurrent.futures import ThreadPoolExecutor as executor
from time import sleep

import tempfile
import os
import folium

__CENTER = [-12.38, -54.92]

__GECKO = './geckodriver'

def builder(**kwargs):

    def image(out, content, template, retry=3):

        os.environ['MOZ_HEADLESS'] = '1'  # -- Uncomment to show driver

        def make(file, data=[]):

            city = folium.Map(location=__CENTER, zoom_start=6)

            polygon = data['polygon']

            folium.Polygon(polygon,  color=data['color'], fill=True,
                        fillColor=data['color'], fillOpacity=1).add_to(city)

            city.save(file)

            return True


        if(retry >= 0):
            file = tempfile.NamedTemporaryFile(mode='w+', suffix='.html')

            if(make(file.name, content)):

                try:
                    driver = webdriver.Firefox(executable_path=__GECKO)

                    driver.set_window_size(1920, 1080)

                    driver.get('file:///' + file.name)

                    sleep(10)

                    driver.save_screenshot(out)
                except:
                    return image(out, content, retry - 1)    

            file.close()

            return {'file': out, 'message': template}

        return {}

    future = executor().submit(
        image, 
        kwargs['out'], 
        kwargs['content'],
        kwargs['template']
    )

    return future
