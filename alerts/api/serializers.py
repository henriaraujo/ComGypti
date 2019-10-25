from rest_framework.serializers import ModelSerializer

from alerts.models import Report, Sensor, Notification, HumiditySensor


class ReportSerializer(ModelSerializer):
    class Meta:
        model = Report
        fields = ('id', 'title', 'description',)


class SensorSerializer(ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id',)


class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id','name')



class HumiditySensorSerializer(ModelSerializer):
    class Meta:
        model = HumiditySensor
        fields = ('id',)