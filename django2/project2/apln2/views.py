from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from apln2.forms import CustomUserCreationForm
# Create your views here.

def base(request):
    return render(request, "base.html")

def home(request):
    return render(request, "home.html")

###########################################################

def signup(request):
    form = CustomUserCreationForm()
    if(request.method == "POST"):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return home(request)
        


    return render(request, "signup.html", {"form": form})
#############################################################


def login1(request):
    if(request.method == "POST"):
        name = request.POST['n']
        password = request.POST['p']
        user = authenticate(username = name, password =  password)
        if user:
            login(request, user)
            return home(request)
        else:
            return HttpResponse("invalid, no user found")
    
    return render(request, "login.html")

        
def logout1(request):
    logout(request)
    return login1(request)

def passwordchange(request):
    return render (request, "password_change_form.html")

def passwordchangedone(request):
    return render (request, "password_change_done.html")