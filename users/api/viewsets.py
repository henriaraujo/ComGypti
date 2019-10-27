from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from users.api.serializers import UserSerializer
from users.models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes_by_action = {
        'create': [AllowAny],
        'auth': [AllowAny]
    }

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]
    # get_permission():
