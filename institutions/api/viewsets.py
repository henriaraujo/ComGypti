from rest_framework.viewsets import ModelViewSet

from institutions.api.serializers import ControlCenterSerializer, InstitutionSerializer
from institutions.models import ControlCenter, Institution


class ControlCenterViewSet(ModelViewSet):
    queryset = ControlCenter.objects.all()
    serializer_class = ControlCenterSerializer


class InstitutionCenterViewSet(ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
