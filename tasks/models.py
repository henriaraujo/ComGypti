from django.db import models

class Measure(models.Model):
    options = {0: 'Call Agents', 1: 'Spray Inseticide', 2: 'ActiveDefenseMechanism'}

    def __str__(self):
        return 'Em construção'

class WorkAssignment(models.Model):
    agentUsernameDesignation = models.CharField(max_length=12)
