from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.files.storage import default_storage
from restapi.models import Department, Employee
from restapi.serializers import DepartmentSerializer, EmployeeSerializer
from rest_framework import generics
@csrf_exempt
def departmentApi(request, id=0):
    if request.method=='GET':
        departments = Department.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method=='POST':
        departments_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=departments_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        
        return JsonResponse("Failed to Add.", safe=False)
    elif request.method=='PUT':
        departments_data = JSONParser().parse(request)
        department = Department.objects.get(DepartmentId=departments_data['DepartmentId'])
        departments_serializer = DepartmentSerializer(department, data=departments_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    elif request.method=='DELETE':
        department = Department.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Succeffully", safe=False)


class DepartmentList(generics.GenericAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    

    def post(self, request):
        departments_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=departments_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        
        return JsonResponse("Failed to Add.", safe=False)
    
    def put(self, request):
        departments_data = JSONParser().parse(request)
        department = Department.objects.get(DepartmentId=departments_data['DepartmentId'])
        departments_serializer = DepartmentSerializer(department,data=departments_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    
    def delete(self, request, id):
        department = Department.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Succeffully", safe=False)
        
    
    
    
class EmployeeList(generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



@csrf_exempt
def employeeApi(request, id=0):
    if request.method=='GET':
        employees = Employee.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
    elif request.method=='POST':
        employees_data = JSONParser().parse(request)
        employees_serializer = EmployeeSerializer(data=employees_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        
        return JsonResponse("Failed to Add.", safe=False)
    elif request.method=='PUT':
        employees_data = JSONParser().parse(request)
        employee = Employee.objects.get(EmployeeId=employees_data['EmployeeId'])
        employees_serializer = EmployeeSerializer(employee, data=employees_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    elif request.method=='DELETE':
        employee = Employee.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Succeffully", safe=False)
    

@csrf_exempt
def SaveFile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)