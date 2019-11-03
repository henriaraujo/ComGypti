from rest_framework.serializers import ModelSerializer

from users.models import User  # , AgentUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email', 'password', 'date_of_birth', 'is_active', 'is_admin',)


'''class AgentUserSerializer(ModelSerializer):
    class Meta:
        model = AgentUser
        fields = ('email', 'date_of_birth', 'password')'''
