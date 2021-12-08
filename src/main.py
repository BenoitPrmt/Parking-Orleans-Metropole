from functions.api_parking import get_parking, search_parking, parking_locate

parkings = get_parking()

for parking in parkings['records']:
    nom = parking['fields']['name']
    places_disponibles = parking['fields']['dispo']
    print(f'{nom} | {places_disponibles} places disponibles')

print('\n')

print(parking_locate())

print('\n')

parking_to_get = input('Parking à rechercher : ')
print(search_parking(parking_to_get))