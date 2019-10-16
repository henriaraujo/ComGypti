from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=12)
    types = [{0: 'MosquitoSensor'}, {1: 'HumiditySensor'}, {2: 'CarbonDioxideSensor'}, {3: 'BrightnessSensor'}]

    def __init__(self,name):
        name = self.name

    def __str__(self):
        return self.name


