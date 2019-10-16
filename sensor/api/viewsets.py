from rest_framework.viewsets import ModelViewSet

from sensor.api.serializers import SensorSerializer
from sensor.models import Sensor

class SensorViewSet(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer