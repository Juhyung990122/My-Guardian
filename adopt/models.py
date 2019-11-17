from django.db import models
from django.conf import settings


class Adopt(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,default = 1, on_delete=models.CASCADE)
    title = models.CharField(max_length = 30)
    image = models.ImageField(max_length=254, blank=True, null=True)
    body = models.TextField()

class Quiz(models.Model):
    title = models.CharField(max_length = 30)
    body = models.TextField()
    answer = models.IntegerField(default = 5)

