from django.shortcuts import render
from django.http import HttpResponse
from .models import Crime

# Create your views here.

def homeView(request):
    crime= Crime.objects.all()
    context={
        "crime":crime
    }
    return render(request,"Home/Home.html")
