from django.db import models

# Create your models here.
class Doctor(models.Model):
    Name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    special = models.CharField(max_length=50)

class Patient(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    mobile = models.IntegerField(null=True)
    address = models.TextField()

class Appointment(models.Model):
    doctor = models.CharField(max_length=55)
    patient = models.CharField(max_length=55)
    date = models.DateField()
    time = models.TimeField() 

class Users (models.Model):
    email = models.CharField(max_length=55)
    uname = models.CharField(max_length=55)
    password = models.CharField(max_length=256)
    role = models.IntegerField(default = 0)

class Appointments(models.Model):
    doctor = models.CharField(max_length=55)
    patient = models.CharField(max_length=55)
    date = models.DateField()
    time = models.TimeField() 


