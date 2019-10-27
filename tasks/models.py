from django.db import models

from institutions.models import PublicEntity


class Measure(models.Model):
    options = {0: 'Call Agents', 1: 'Spray Inseticide', 2: 'ActiveDefenseMechanism'}
    public_entity = models.ForeignKey(PublicEntity, on_delete=models.CASCADE)

    # def __init__(self):
    #    self.app_label = 'measure'

    def __str__(self):
        return 'Em construção'

    class Meta:
        app_label = 'tasks'


class WorkAssignment(models.Model):
    agentUsernameDesignation = models.CharField(max_length=12)
    public_entity = models.ForeignKey(PublicEntity, on_delete=models.CASCADE)

    class Meta:
        app_label = 'tasks'
