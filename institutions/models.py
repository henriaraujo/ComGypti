from django.db import models



class Institution(models.Model):
    name = models.CharField(max_length=12)


    def __init__(self):
        self.app_label = 'institutions'

class ControlCenter(Institution):
    pass

    def __init__(self):
        self.app_label = 'institutions'

class CentralEntity(Institution):
    pass

    def __init__(self):
        self.app_label = 'institutions'

class PublicEntity(Institution):
    pass

    def __init__(self):
        self.app_label = 'institutions'