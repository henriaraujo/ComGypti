from django.contrib import admin

from institutions.models import Institution, ControlCenter, CentralEntity, PublicEntity

admin.site.register(Institution)
admin.site.register(ControlCenter)
admin.site.register(CentralEntity)
admin.site.register(PublicEntity)
