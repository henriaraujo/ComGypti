"""comgypti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from alerts.api.viewsets import ReportViewSet, SensorViewSet, NotificationViewSet, HumiditySensorViewSet, \
    MosquitoSensorViewSet, CarbonDioxideSensorViewSet, BrightnessSensorViewSet
# from users.api.viewsets import UserViewSet
from institutions.api.viewsets import ControlCenterViewSet
from tasks.api.viewsets import MeasureViewSet, WorkAssignmentViewSet
from tasks.models import WorkAssignment
from users.api.viewsets import UserViewSet

router = routers.DefaultRouter()
# router.register('users', PontoTuristicoViewSet, base_name='ComGypti')
# router.register('users', UserViewSet)


router.register('reports', ReportViewSet)
router.register('notifications', NotificationViewSet)

router.register('sensors', SensorViewSet)
router.register('humitysensors', HumiditySensorViewSet)
router.register('mosquitosensors', MosquitoSensorViewSet)
router.register('carbondioxidesensors', CarbonDioxideSensorViewSet)
router.register('brightnesssensors', BrightnessSensorViewSet)


router.register('users', UserViewSet)

router.register('measures', MeasureViewSet)
router.register('workassignments', WorkAssignmentViewSet)
router.register('controlcenters', ControlCenterViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
]  # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
