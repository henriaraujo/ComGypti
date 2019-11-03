from rest_framework.permissions import BasePermission
from rest_framework.viewsets import ModelViewSet

from users.api.serializers import UserSerializer #, AgentUserSerializer
from users.models import User


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_admin)



class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


'''class AgentUserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AgentUserSerializer'''



# authentication_classes = (TokenAuthentication,)
# permission_classes = (IsAuthenticated,)


# def create(self, request, *args,**kwargs):
#    pass


'''class AgentViewSet(ModelViewSet):
    queryset = AgentUser.objects.all()
    serializer_class = AgentUserSerializer

   # authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)


    #def create(self, request, *args,**kwargs):
    #    pass'''
