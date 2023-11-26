from django.shortcuts import render
from app8.models import *
from app8.forms import *
# Create your views here.

def base(request):
    return render(request, "base.html")

def add(request):
    s = EmployeeForm()
    if request.method == "POST":
        s = EmployeeForm(request.POST)
        if s.is_valid():
            s.save()
            return view(request)
    return render(request, "add.html", {'form':s})

def view(request):
    d = Employee.objects.all()
    context = {"data": d}
    return render(request, "views.html", context)

def edit(request, p):
    b = Employee.objects.get(pk=p)
    form = EmployeeForm(instance=b)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=b)
        if form.is_valid():
            form.save()
            return view(request)
    return render(request, 'edit.html', {'form' : form})

def delete(request, p):
    b = Employee.objects.get(pk=p)
    b.delete()
    return view(request)
