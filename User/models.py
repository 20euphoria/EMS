from statistics import mode
from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.AutoField(primary_key=True, unique=True)
    ename = models.CharField(max_length=80)
    ecity = models.CharField(max_length=80)
    etype = models.CharField(max_length=80)
    edomain = models.CharField(max_length=80)
