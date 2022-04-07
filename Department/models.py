from operator import mod
from statistics import mode
from django.db import models
from User.models import Employee, EmployeeSerializers
from rest_framework import serializers

# Create your models here.
class Department(models.Model):
    deptid = models.AutoField(primary_key=True, unique=True)
    eid = models.ForeignKey(Employee, on_delete=models.CASCADE)
    deptname = models.CharField(max_length=80)

    def __repr__(self) -> str:
        return f"{self.eid}"

class DepartmentSerializer(serializers.ModelSerializer):
    eid = EmployeeSerializers()
    class Meta:
        model = Department
        fields = '__all__'