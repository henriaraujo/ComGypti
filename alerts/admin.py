from django.contrib import admin

from alerts.models import Report, Notification, Sensor, HumiditySensor, CarbonDioxideSensor, BrightnessSensor, \
    MosquitoSensor

admin.site.register(Report)
admin.site.register(Notification)
#admin.site.register(Sensor)
admin.site.register(HumiditySensor)
admin.site.register(CarbonDioxideSensor)
admin.site.register(BrightnessSensor)
admin.site.register(MosquitoSensor)

