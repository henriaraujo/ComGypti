from rest_framework.viewsets import ModelViewSet

from alerts.api.serializers import NotificationSerializer
from tasks.api.serializers import MeasureSerializer
from tasks.models import Measure, WorkAssignment


class MeasureViewSet(ModelViewSet):
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializer
  #  authentication_classes = (TokenAuthentication,)
   # permission_classes = (IsAuthenticated, IsResponsible)


class WorkAssignmentViewSet(ModelViewSet):
    queryset = WorkAssignment.objects.all()
    serializer_class = NotificationSerializer
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated, IsAgent)


