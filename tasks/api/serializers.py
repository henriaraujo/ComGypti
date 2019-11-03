from rest_framework.serializers import ModelSerializer

from tasks.models import Measure, WorkAssignment


class MeasureSerializer(ModelSerializer):
    class Meta:
        model = Measure
        fields = ('id',)


class WorkAssignmentSerializer(ModelSerializer):
    class Meta:
        model = WorkAssignment
        fields = ('id',)
