from django.db import models

# Create your models here.
class NonVegClassicModel(models.Model):
    Pizza = models.CharField(max_length=35)
    Small = models.IntegerField()
    Medium = models.IntegerField()
    Large = models.IntegerField()