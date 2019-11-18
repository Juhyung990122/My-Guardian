from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    score = models.IntegerField(default = 0)
    test_pass = models.BooleanField(default=False)