import googlemaps

class Map:
    mapsKey = 'AIzaSyAl_OhUmGOTt-c1Zt1y9ne0M8MXlc5Sotg'
    gmaps = googlemaps.Client(key=mapsKey)


class Localisation:
    sensor_alert_localization = Map.gmaps.reverse_geocode((40.714224, -73.961452))
