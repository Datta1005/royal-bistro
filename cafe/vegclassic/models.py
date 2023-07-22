from django.db import models
# Create your models here.
class ClassicInfoModel(models.Model):
    Pizza = models.CharField(max_length=35)
    Small = models.IntegerField(null=True)
    Medium = models.IntegerField(null=True)
    Large = models.IntegerField(null=True)


# Create your models here.
