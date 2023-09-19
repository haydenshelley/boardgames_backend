import datetime

from django.db import models
from django.utils import timezone


class Boardgame(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    player = models.CharField(max_length=50)
    def __str__(self):
        return self.name