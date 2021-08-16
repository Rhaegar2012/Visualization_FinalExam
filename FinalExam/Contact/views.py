from django.shortcuts import render
from .models import Contact 
# Create your views here.
def contactView(request):
    contacts=Contact.objects.all()
    context ={
        "contacts":contacts
    }
    return render(request,"Contact/Contact.html",context)
