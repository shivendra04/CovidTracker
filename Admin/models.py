from django.db import models

# Create your models here.
class registerAdmin(models.Model):
    name = models.CharField(max_length = 50)
    phoneNumber = models.IntegerField()
    pinCode = models.IntegerField()
