from django.db import models


# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    emp_id = models.AutoField(primary_key=True)  # Use AutoField with primary_key=True
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.TextField()
    dept = models.CharField(max_length=100)
    salary = models.IntegerField(default=0)
    location = models.CharField(max_length=100, default='Delhi')
    role = models.CharField(max_length=100)
    hire_date = models.DateField()

    def __str__(self):
        return self.name
