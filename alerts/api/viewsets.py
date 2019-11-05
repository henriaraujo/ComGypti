from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authentication import TokenAuthentication
from alerts.api.serializers import ReportSerializer, SensorSerializer, NotificationSerializer, HumiditySensorSerializer, \
    CarbonDioxideSensorSerializer, MosquitoSensorSerializer, BrightnessSensorSerializer
from rest_framework.viewsets import ModelViewSet

from alerts.models import Report, Sensor, Notification, HumiditySensor, CarbonDioxideSensor, MosquitoSensor, \
    BrightnessSensor
from data.models import Map, Localisation


class ReportViewSet(ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    authentication_classes = (TokenAuthentication,)


# permission_classes = (IsAuthenticated, IsResponsible)


@receiver(post_save, sender=Report)
def generate_directions(**kwargs):
    last_reported_saved = Report.objects.filter().order_by('-id')[0]
    a = Report.objects.filter(id=last_reported_saved.id)
    geocode_directions_origin = Map.gmaps.geocode(a.latest('id').control_center_city.address)
    geocode_directions_destin = Map.gmaps.geocode(a.latest('id').origin_address_problem)
    a.update(geocode_destin=geocode_directions_destin)
    a.update(geocode_origin=geocode_directions_origin)

    loc = Localisation()
    a.update(way_to_report_problem=loc.give_directions(last_reported_saved.origin_address_problem,
                                                       last_reported_saved.control_center_city.address))


class NotificationViewSet(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    # authentication_classes = (TokenAuthentication,)


# permission_classes = (IsAuthenticated, IsAgent)


class SensorViewSet(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class HumiditySensorViewSet(SensorViewSet):
    queryset = HumiditySensor.objects.all()
    serializer_class = HumiditySensorSerializer


class CarbonDioxideSensorViewSet(SensorViewSet):
    queryset = CarbonDioxideSensor.objects.all()
    serializer_class = CarbonDioxideSensorSerializer


class MosquitoSensorViewSet(SensorViewSet):
    queryset = MosquitoSensor.objects.all()
    serializer_class = MosquitoSensorSerializer


class BrightnessSensorViewSet(SensorViewSet):
    queryset = BrightnessSensor.objects.all()
    serializer_class = BrightnessSensorSerializer
