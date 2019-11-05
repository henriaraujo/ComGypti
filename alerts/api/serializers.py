from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from alerts.models import Report, Sensor, Notification, HumiditySensor, CarbonDioxideSensor, MosquitoSensor, \
    BrightnessSensor


class ReportSerializer(ModelSerializer):
    control_center_city = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Report
        fields = '__all__'


class NotificationSerializer(ModelSerializer):
    report = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    public_entity = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Notification
        fields = '__all__'


class SensorSerializer(ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'


class HumiditySensorSerializer(ModelSerializer):
    class Meta:
        model = HumiditySensor
        fields = '__all__'


class MosquitoSensorSerializer(ModelSerializer):
    class Meta:
        model = MosquitoSensor
        fields = '__all__'


class CarbonDioxideSensorSerializer(ModelSerializer):
    class Meta:
        model = CarbonDioxideSensor
        fields = '__all__'


class BrightnessSensorSerializer(ModelSerializer):
    class Meta:
        model = BrightnessSensor
        fields = '__all__'
