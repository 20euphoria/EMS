import re
from traceback import print_tb
from urllib import request
from django.shortcuts import redirect, render
from .models import Department, DepartmentSerializer
from User.models import Employee, EmployeeSerializers
from rest_framework.decorators import api_view
# from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# token = Token.objects.create(user = )
# print(token)

# Create your views here.
@api_view(['GET'])
def get_data(request):
    emp_data = Department.objects.filter(eid__user = request.user)
    ser = DepartmentSerializer(emp_data, many=True).data
    print(emp_data)
    print(ser)
    # for d in emp_data:
        # print(d.department.deptname)
    emp_id = Employee.objects.all()
    # emp_ser = EmployeeSerializers(emp_id, many=True).data
    context = {"data": ser, 'emp':emp_id}
    return render(request, "templates/home.html", context)

@api_view(["GET","POST","PUT"])
def post_dept(request):
    emp_data = Department.objects.filter(eid__user = request.user)
    ser = DepartmentSerializer(emp_data, many=True).data
    emp_id = Employee.objects.all()
    emp_ser = EmployeeSerializers(emp_id, many=True).data
    print(request.data)
    method = request.method
    if method == "POST":
        emp_id = int(request.POST['emp_id'])
        emp_obj = Employee.objects.get(eid=emp_id)
        dept_name = request.POST['dept_name']
        if Department.objects.filter(eid__iexact=emp_obj, deptname__iexact=dept_name).exists():
            return redirect("get_data")
        else:
            dept = Department(eid=emp_obj, deptname=dept_name)
            dept.save()
            return redirect("get_data")
    context = {"data": ser, 'emp':emp_ser}
    return render(request, 'templates/home.html', context)