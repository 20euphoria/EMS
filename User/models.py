from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers

# Create your models here.


class Employee(models.Model):
    eid = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ename = models.CharField(max_length=80)
    ecity = models.CharField(max_length=80)
    etype = models.CharField(max_length=80)
    edomain = models.CharField(max_length=80)

    def __str__(self) -> str:
        return f"{self.eid} - {self.edomain}"

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"