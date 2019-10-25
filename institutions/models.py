from django.db import models



class Institution(models.Model):
    name = models.CharField(max_length=12)


class ControlCenter(Institution):
    pass


class CentralEntity(Institution):
    pass


class PublicEntity(Institution):
    pass
