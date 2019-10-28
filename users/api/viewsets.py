from rest_auth.registration.views import RegisterView

from users.models import User


class CustomRegisterView(RegisterView):
    queryset = User.objects.all()
