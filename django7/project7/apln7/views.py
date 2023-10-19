from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home.html")

def signup(request):
    return render(request, "signup.html")

def signin(request):
    return render(request, "signin.html")

# @login_required
def drag(request):
    return render(request, "dragdrop.html",)