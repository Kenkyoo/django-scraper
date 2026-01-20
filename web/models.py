from django.contrib.auth.models import User
from django.db import models


class Image(models.Model):
    url = models.URLField()


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
