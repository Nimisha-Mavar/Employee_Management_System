from django.shortcuts import render
from .models import Employee
from django.contrib import messages
# Create your views here.
def home(request):
    emps=Employee.objects.all()
    if request.method=='POST':
        if "add" in request.POST:
            name=request.POST.get("name")
            email=request.POST.get("name")
            role=request.POST.get("role")

            newEmp=Employee.objects.create(
                name=name,email=email,role=role
            )

            messages.success(request,"Employee Created Successfully")
    context={
        "Employees":emps
    }
    return render(request,'index.html',context)