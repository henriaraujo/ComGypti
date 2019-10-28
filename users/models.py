from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import datetime

from users.userModel import UserManager


class User(AbstractBaseUser):
    username = None
    email = models.EmailField('email address', unique=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(default=datetime.date.today)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'name']

    objects = UserManager()


    def __str__(self):  # __unicode__ on Python 2
        return self.email

    class Meta:
        app_label = 'users'
