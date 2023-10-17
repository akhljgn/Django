from django.shortcuts import render

# Create your views here.
def drag(request):
    return render(request, "dragdrop.html",)