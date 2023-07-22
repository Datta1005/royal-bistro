from django.db import models

# Create your models here.
class VegInfoModel(models.Model):
    Burger = models.CharField(max_length=25)
    prize = models.IntegerField()
