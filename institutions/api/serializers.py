from rest_framework.serializers import ModelSerializer

from institutions.models import ControlCenter


class InstitutionSerializer(ModelSerializer):
    class Meta:
        model = ControlCenter
        fields = ('id',)


class ControlCenterSerializer(ModelSerializer):
    class Meta:
        model = ControlCenter
        fields = ('id',)
