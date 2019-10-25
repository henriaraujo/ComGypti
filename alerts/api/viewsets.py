from rest_framework.viewsets import ModelViewSet

from alerts.api.serializers import ReportSerializer, SensorSerializer, NotificationSerializer, HumiditySensorSerializer
from rest_framework.viewsets import ModelViewSet

from alerts.models import Report, Sensor, Notification, HumiditySensor


class ReportViewSet(ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class SensorViewSet(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class HumiditySensorViewSet(SensorViewSet):
    queryset = HumiditySensor.objects.all()
    serializer_class = HumiditySensorSerializer


class NotificationViewSet(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
