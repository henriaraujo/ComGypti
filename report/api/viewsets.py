from rest_framework.viewsets import ModelViewSet

from report.api.serializers import ReportSerializer
from report.models import Report


class ReportViewSet(ModelViewSet):
    queryset = Report.object.all()
    serializer_class = ReportSerializer