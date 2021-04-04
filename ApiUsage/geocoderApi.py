from pygeocoder import Geocoder

API_KEY = ''

address = '1222, Lins de Vasconcelos, São Paulo, SP'
coordinates = Geocoder(API_KEY).geocode(address).coordinates

print(coordinates)
