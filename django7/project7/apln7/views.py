from django.shortcuts import render
from apln7.forms import loginForm

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

def form2(request):
    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            form.save()
            return home(request)
    return render (request, "signin.html")