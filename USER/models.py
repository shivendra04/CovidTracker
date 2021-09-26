from django.db import models

# Create your models here.
class registerUser(models.Model):
    name = models.CharField(max_length = 50)
    phoneNumber = models.IntegerField()
    pinCode = models.IntegerField()

class SelfAssessment(models.Model):
    symptom = models.CharField(max_length = 50)
    travelHistory = models.BooleanField()
    contactWithCovidPatient = models.BooleanField()
