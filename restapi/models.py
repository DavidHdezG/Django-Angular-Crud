from django.db import models

# Create your models here.
class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date_of_joining = models.DateField()
    photo_filename = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name