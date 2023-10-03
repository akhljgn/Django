from django.shortcuts import render, redirect
# from django.http import HttpResponse
from apln3.models import Employee
from apln3.forms import EmployeeForm

# Create your views here.

def base(request):
    return render(request, "base.html")

def home(request):
    return render(request, "home.html")

def addemp(request):
    form = EmployeeForm()
    if(request.method == "POST"):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return views(request)
        else:
            form = EmployeeForm()
    return render(request, "addemp.html", {"form": form})

def views(request):
    viewpage = Employee.objects.all()
    return render (request, "views.html", {"employee": viewpage})

def editemp(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("views")
    context = {
        "employee": employee,
        'form': form,
    }
    return render(request, "edit.html", context)

def empdelete(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == "POST":
        employee.delete()
        return redirect("views")
    context = {
        "employee": employee,
    }
    return render(request, "delete.html", context)

def empview(request, pk):
    employee = Employee.objects.get(id=pk)
    context = {
        "employee": employee,
    }
    return render(request, "employeeview.html", context)