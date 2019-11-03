from rest_framework.serializers import ModelSerializer

from alerts.models import Report, Sensor, Notification, HumiditySensor, CarbonDioxideSensor, MosquitoSensor, \
    BrightnessSensor


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
        fields = ('id', 'name')


class HumiditySensorSerializer(ModelSerializer):
    class Meta:
        model = HumiditySensor
        fields = ('id',)


class MosquitoSensorSerializer(ModelSerializer):
    class Meta:
        model = MosquitoSensor
        fields = ('id',)


class CarbonDioxideSensorSerializer(ModelSerializer):
    class Meta:
        model = CarbonDioxideSensor
        fields = ('id',)


class BrightnessSensorSerializer(ModelSerializer):
    class Meta:
        model = BrightnessSensor
        fields = ('id',)
