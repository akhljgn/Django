from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from.forms import BookCreate
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

def login(request):
    return render(request, "loginform.html")