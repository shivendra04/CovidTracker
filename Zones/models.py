from django.db import models

# Create your models here.
class ZoneDetail(models.Model):
    name = models.CharField(max_length = 50)
    pinCode = models.IntegerField()
    zoneType = models.CharField(max_length = 50)
    numCases = models.IntegerField()
