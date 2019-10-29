from rest_framework.viewsets import ModelViewSet


class ReportViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
   # authentication_classes = (TokenAuthentication,)
   # permission_classes = (IsAuthenticated,)
