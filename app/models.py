from django.db import models

# Create your models here.


class Patient(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

    

class Intervention(models.Model):
    intervention_date = models.DateField()
    diagnostic = models.CharField(max_length=100)
    procedure_name = models.CharField(max_length=100)


class Procedure(models.Model):
    name = models.CharField()
