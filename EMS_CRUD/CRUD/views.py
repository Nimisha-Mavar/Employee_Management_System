from django.shortcuts import render
from .models import Employee
# Create your views here.
def home(request):
    emps=Employee.objects.all()
    context={
        "Employees":emps
    }
    return render(request,'index.html',context)