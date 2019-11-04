from django.db import models


# Vai ficar na central Db

class Institution(models.Model):
    name = models.CharField(max_length=12)
    address = models.TextField(max_length=500)

    def __str__(self):
        return str(self.id) + ' - ' + self.name

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
