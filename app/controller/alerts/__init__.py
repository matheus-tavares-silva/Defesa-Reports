from app.controller.alerts.data import data
from ..folder import folder
from glob import glob

import folium
import imgkit
import tempfile
import os

__OPTIONS = {
    'xvfb': ''
}

__NAME = 'alert'

__CENTER = [-12.68, -56.92]


def alerts():
    path = '{}/{}-*.jpg'.format(folder('Alerts'), __NAME)

    alerts = []

    contents = data()

    for index, content in enumerate(contents):
        out = path.replace('*', str(index + 1))
        
        file = tempfile.NamedTemporaryFile(mode='w+', suffix='.html')        


        build(file.name, content)

        imgkit.from_file(
            file.name,
            out,
            options=__OPTIONS
        )

        file.close()

        alerts.append({'file' : out, 'content' : content})

    return alerts

def build(file, data=[]):

    city = folium.Map(location=__CENTER, zoom_start=5)

    polygon = data['polygon']

    folium.Polygon(polygon,  color=data['color'], fill=True, fillColor=data['color'], fillOpacity=1).add_to(city)

    city.save(file)

    return None

if __name__ == "__main__":
    alerts()