from django.db import models


class Report(models.Model):
    title = models.CharField(max_length=12)
    description = models.TextField(max_length=800)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'report'
