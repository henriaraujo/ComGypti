from django.db import models


class Report(models.Model):
    title = models.CharField(max_length=12)
    description = models.TextField(max_length=800)

    def __str__(self):
        return self.title

    # class Meta:
    #     app_label = 'report'


class Notification(models.Model):
    name = models.CharField(max_length=12)

    def __str__(self):
        return self.name

    # class Meta:
    #     app_label = "notification"


class Sensor(models.Model):
    name = models.CharField(max_length=12)
    tolerance_to_make_a_alert = models.FloatField(max_length=12)




class HumiditySensor(Sensor):
    pass


class MosquitoSensor(Sensor):
    frequency_list = ['minute', 'hour', 'day']
    MINUTE = 'M'
    HOUR = 'H'
    DAY = 'D'
    FREQUENCY_LIST_CHOICES = [
        (MINUTE, 'Minute'),
        (HOUR, 'Hour'),
        (DAY, 'Day'),
    ]
    mosquito_sensor_frequency = models.CharField(
        max_length=1,
        choices=FREQUENCY_LIST_CHOICES,
        default=DAY,
    )


class BrightnessSensor(Sensor):
    pass


class CarbonDioxideSensor(Sensor):
    pass
