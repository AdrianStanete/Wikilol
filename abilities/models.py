from django.db import models

# Create your models here.
from champions.models import Champion


class Ability(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.CharField(max_length=256, unique=True)
    power = models.IntegerField()
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE)