import googlemaps
from django.db import models

class Map:
    gmaps = googlemaps.Client(key='AIzaSyAl_OhUmGOTt-c1Zt1y9ne0M8MXlc5Sotg')

    def __str__(self):
        return self.gmaps
