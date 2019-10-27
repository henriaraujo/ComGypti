from django.db import models


class Institution(models.Model):
    name = models.CharField(max_length=12)

    class Meta:
        app_label = 'institutions'


class ControlCenter(Institution):
    pass

    class Meta:
        app_label = 'institutions'


class CentralEntity(Institution):
    pass

    class Meta:
        app_label = 'institutions'


class PublicEntity(Institution):
    pass

    class Meta:
        app_label = 'institutions'
