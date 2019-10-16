from rest_framework.serializers import ModelSerializer

from report.models import Report


class ReportSerializer(ModelSerializer):
    class Meta:
        model = Report
        fields = ('id','name','description',)
