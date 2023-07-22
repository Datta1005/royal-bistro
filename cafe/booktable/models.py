from django.db import models

# Create your models here.
class BookTableModel(models.Model):
    Name = models.CharField(max_length=25)
    Add = models.CharField(max_length=50)
    Person = models.IntegerField()