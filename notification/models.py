from django.db import models

class Notification(models.Model):
    name = models.CharField(max_length=12)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "notification"

