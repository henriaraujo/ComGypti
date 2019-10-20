from rest_framework.viewsets import ModelViewSet

from alerts.api.serializers import ReportSerializer, SensorSerializer, NotificationSerializer
from rest_framework.viewsets import ModelViewSet

from alerts.models import Report, Sensor, Notification


class ReportViewSet(ModelViewSet):
    queryset = Report.object.all()
    serializer_class = ReportSerializer


class SensorViewSet(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class NotificationViewSet(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
