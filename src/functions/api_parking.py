import requests
import json
import folium
from config import API_LINK, DEFAULT_MAP_ZOOM, DEFAULT_MAP_CENTER

def get_parking():
    """Récupère tous les parkings d'Orléans

    Returns:
        JSON: All parkings
    """

    p = requests.get(API_LINK)
    return p.json()

parkings = get_parking()

def search_parking(park):
    """Recherche un parking dans la liste et donne les places disponibles

    Args:
        park (str): Nom du parking (nom exact)

    Returns:
        str: Nom et places disponibles
    """

    for parking in parkings['records']:
        nom = parking['fields']['name']

        if nom.lower() == park.lower():
            places_disponibles = parking['fields']['dispo']
            return f'{nom} | {places_disponibles} places disponibles'
        else:
            pass

    return f'Le parking {park} n\'existe pas !'



def parking_locate():
    """Affiche la carte des parkings d'Orléans-Métropole dans un fichier 'map.html'
    """
    map_osm = folium.Map(location=[DEFAULT_MAP_CENTER['lat'], DEFAULT_MAP_CENTER['long']], zoom_start = DEFAULT_MAP_ZOOM)

    for park in parkings['records']:

        coos = park['fields']["coords"].split(',')
        # coos.reverse()

        if int(park['fields']['dispo']) >= 30:
            color = 'green'
        elif int(park['fields']['dispo']) > 0:
            color = 'orange'
        else:
            color =  'red'

        text_popup = f'{park["fields"]["name"]}<br> {park["fields"]["dispo"]}/{park["fields"]["total"]}'

        folium.Marker(
           location=coos,
           popup = folium.Popup(text_popup, max_width=200),
           icon = folium.Icon(color=color, icon='parking')
        ).add_to(map_osm)

    map_osm.save('map.html')
    return f'Le fichier "map.html" a été mis à jour !'

if __name__ == "__main__":
    print(json.dumps(get_parking(), indent=4))

    parking_locate()