from django.shortcuts import render
from django.http import HttpResponse
from apln4.models import CustUser
from apln4.forms import CustUserCreationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def base(request):
    return render(request, "base.html")

def home(request):
    return render(request, "home.html")

def signup(request):
    form = CustUserCreationForm()
    if(request.method == "POST"):
        form = CustUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return signin(request)
    return render(request, "signup.html", {"form": form})

def signin(request):
    if(request.method == "POST"):
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(username = name, password =  password)
        if user:
            login(request, user)
            return home(request)
        else:
            return HttpResponse("invalid, no user found")
    return render(request, "signin.html")

        
def signout(request):
    logout(request)
    return signin(request)

def viewuser(request, pk):
    Custuser = CustUser.objects.get(id=pk)
    context = {
        "user": Custuser,
    }
    return render(request, "UserView.html", context)