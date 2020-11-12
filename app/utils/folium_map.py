import folium
import tempfile

def build_folium_map(default_location=[-12.38, -54.92], data=[], zoom=6):

    city = folium.Map(location=default_location, zoom_start=zoom)

    folium.Polygon(
        data['polygon'],  
        color=data['color'], 
        fill=True, 
        fillColor=data['color'], 
        fillOpacity=1
    ).add_to(city)

    with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as file_temp:

        city.save(file_temp.name)

    

    return file_temp.name
    