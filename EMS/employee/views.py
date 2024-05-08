from django.shortcuts import render,HttpResponse
from .models import Employee
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'index.html')
# Path: employee/templates/index.html

def add(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']
        dept=request.POST['dept']
        salary=request.POST['salary']
        location=request.POST['location']
        role=request.POST['role']
        hire_date=request.POST['hire_date']
        emp=Employee(name=name,email=email,phone=phone,address=address,dept=dept,salary=salary,location=location,role=role,hire_date=hire_date)
        emp.save()
        return render(request,'index.html')
    elif request.method=='GET':   
        return render(request, 'add.html')
    else:
        return HttpResponse('Invalid Request')
    
def view(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
        }
    print(context)
    return render(request,'view.html',context)
def remove(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
        }
    print(context)
    return render(request,'index.html',context)

def filter(request):
    if request.method=='POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        location=request.POST['location']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(name__icontains=name))
        if dept:
            emps=emps.filter(dept__icontains=dept) 
        if role:
            emps=emps.filter(role__icontains=role)
        if location:
            emps=emps.filter(location__icontains=location)
        
        context={
            'emps':emps
            }   
        return render(request,'view.html',context)
    elif request.method=='GET':     
        return render(request,'filter.html')
    else:
        return HttpResponse('Invalid Request')
def delete(request,emp_id=0):
    if emp_id:
        try:
            emp=Employee.objects.get(emp_id=emp_id)
            emp.delete()
            return render(request,'index.html')
        except:
            return HttpResponse('Invalid Employee ID')
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'delete.html',context)