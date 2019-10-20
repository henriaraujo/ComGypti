from django.db import models


class Report(models.Model):
    title = models.CharField(max_length=12)
    description = models.TextField(max_length=800)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'alert'


class Notification(models.Model):
    name = models.CharField(max_length=12)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "alert"


class Sensor(models.Model):
    name = models.CharField(max_length=12)
    types = [{0: 'MosquitoSensor'}, {1: 'HumiditySensor'}, {2: 'CarbonDioxideSensor'}, {3: 'BrightnessSensor'}]

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'alert'

