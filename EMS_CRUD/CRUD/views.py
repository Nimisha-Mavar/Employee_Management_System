from django.shortcuts import render
from .models import Employee
from django.contrib import messages
from django.db.models import Q
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
            newEmp.save()
            messages.success(request,"Employee Created Successfully")
        elif "update" in request.POST:
            name=request.POST.get("name")
            email=request.POST.get("email")
            role=request.POST.get("role")
            eid=request.POST.get("id")

            update_emp=Employee.objects.get(id=eid)
            update_emp.name=name
            update_emp.email=email
            update_emp.role=role
            update_emp.save()
            messages.success(request,"Employee Updated Successfully")
        elif "delete" in request.POST:
            eid=request.POST.get("id")
            Employee.objects.get(id=eid).delete()
            messages.success(request,"Employee Deleted Successfully")

        elif "search" in request.POST:
           quary=request.POST.get("searchQuery") 
           emps=Employee.objects.filter(Q(name__icontains=quary)|Q(email__icontains=quary)|Q(role__icontains=quary))
    context={
        "Employees":emps
    }
    return render(request,'index.html',context)