from django.contrib import admin

from alerts.models import Report, Notification, Sensor

admin.site.register(Report)
admin.site.register(Notification)
admin.site.register(Sensor)
