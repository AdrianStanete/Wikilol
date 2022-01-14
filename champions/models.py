from django.db import models
from django.db.models.aggregates import Max


# Create your models here.

class Champion(models.Model):
    name = models.CharField(max_length=256, unique=True)
    hability_power = models.IntegerField()


class Ability(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.CharField(max_length=256, unique=True)
    power = models.IntegerField()
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE)
