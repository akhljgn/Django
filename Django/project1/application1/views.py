from django.shortcuts import render
from django.http import HttpResponse
from application1.models import student
from application1.forms import studentForm

# Create your views here.

def home(request):
    return HttpResponse("hello django")

def index(request):
    return render(request, "index.html")

def index1(request):
    return render(request, "index1.html")

###################################################

def form1(request):
    form = studentForm()
    if request.method == "POST":
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            return list1(request)
        else:
            form = studentForm()
    return render(request, "form1.html", {"form": form})


def form2(request):
    if request.method == "POST":
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            return list1(request)
    return render (request, "form2.html")

def form3(request):
    if request.method == "POST":
        n = request.POST[ 'name' ]
        a = request.POST[ 'age' ]
        o = student.objects.create(name = n, age = a)
        o.save()
        return list1(request)
    return render (request, "form3.html")

#######################################################

def list1(request):
    k = student.objects.all()
    return render (request, "list.html", {"s": k})