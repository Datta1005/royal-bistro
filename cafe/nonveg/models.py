from django.db import models

# Create your models here.
class NonVegInfoModel(models.Model):
    Burger = models.CharField(max_length=40)
    prize = models.IntegerField()
