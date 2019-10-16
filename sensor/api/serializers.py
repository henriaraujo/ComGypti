from rest_framework.serializers import ModelSerializer

from sensor.models import Sensor


class SensorSerializer(ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id','type')
