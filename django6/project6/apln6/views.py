from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from.forms import BookCreate
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def upload(request):
    upload = BookCreate()
    if request.method == "POST":
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""Your form is wrong, reload on <a href="{{ url 'index' }}">Reload</a> """)
    else:
        return render(request, "upload_form.html", {"upload_form": upload})
    
def index(request):
    shelf = Book.objects.all()
    return render(request, "list.html", {"shelf": shelf})


# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        if request.method == "POST":
            username = request.POST.get("uname")
            email = request.POST.get("email")
            password = request.POST.get("pswd")
            cpass = request.POST.get("cpswd")
            if password == cpass:
                if User.objects.filter(username=username, email=email).exists():
                    messages.info(request, "username already taken")
                    print("already have")
                else:
                    new_user = User.objects.create_user(username, email, password)
                    new_user.save()
                    return redirect(loginpage)
            else:
                print("Wrong password")
        return render(request, "loginform.html.html")
    

def loginpage(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username = username, password = password)
            if user is not True:
                login(request, user)
                return redirect(homepage)
            else:
                messages.info(request, "user not exists")
                print("User not exists")
                return redirect(loginpage)
    return render(request, "loginform.html")

def homepage(request):
    return render(request, "home.html")
    
@login_required
def userlogoout(request):
    logout(request)
    return redirect(loginpage)