from rest_framework.serializers import ModelSerializer

from users.models import User  # , AgentUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



'''class AgentUserSerializer(ModelSerializer):
    class Meta:
        model = AgentUser
        fields = ('email', 'date_of_birth', 'password')'''
