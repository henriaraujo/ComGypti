from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from alerts.api.serializers import ReportSerializer, SensorSerializer, NotificationSerializer, HumiditySensorSerializer,\
    CarbonDioxideSensorSerializer, MosquitoSensorSerializer, BrightnessSensorSerializer
from rest_framework.viewsets import ModelViewSet

from alerts.models import Report, Sensor, Notification, HumiditySensor, CarbonDioxideSensor, MosquitoSensor, \
    BrightnessSensor


class ReportViewSet(ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    authentication_classes = (TokenAuthentication,)
   # permission_classes = (IsAuthenticated, IsResponsible)


class NotificationViewSet(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    authentication_classes = (TokenAuthentication,)
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
