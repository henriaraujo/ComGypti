from django.db import models

from institutions.models import PublicEntity


class Measure(models.Model):
    options = ('Call Agents', 'Spray Inseticide', 'ActiveDefenseMechanism',)
    public_entity = models.ForeignKey(PublicEntity, on_delete=models.CASCADE)

    class Meta:
        app_label = 'tasks'


class WorkAssignment(models.Model):
    agentUsernameDesignation = models.CharField(max_length=12)
    public_entity = models.ForeignKey(PublicEntity, on_delete=models.CASCADE)

    class Meta:
        app_label = 'tasks'
