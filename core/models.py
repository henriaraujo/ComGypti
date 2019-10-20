import googlemaps


class Map:
    mapsKey = 'AIzaSyAl_OhUmGOTt-c1Zt1y9ne0M8MXlc5Sotg'
    gmaps = googlemaps.Client(key=mapsKey)

    def __str__(self):
        return self.gmaps
