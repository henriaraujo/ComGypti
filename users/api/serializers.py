from users.models import User


class UserSerializer:
    class Meta:
        model = User
        fields = ('email')
