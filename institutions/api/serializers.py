from rest_framework.serializers import ModelSerializer

from institutions.models import ControlCenter


class InstitutionSerializer(ModelSerializer):
    class Meta:
        model = ControlCenter
        fields = '__all__'


class ControlCenterSerializer(ModelSerializer):
    class Meta:
        model = ControlCenter
        fields = '__all__'
