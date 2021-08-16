from os import name
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Contact 
from .forms import UserRegisterForm
from django.core.mail import send_mail

# Create your views here.
def contactView(request):
    contacts=Contact.objects.all()
    context ={
        "contacts":contacts
    }
    return render(request,"Contact/register.html",context)

def register(request):
    if request.method == 'POST':
      form = UserRegisterForm(request.POST)
      if form.is_valid(): 
        form.save()
        username = form.cleaned_data.get('username')
        send_mail(subject='New User', message='You have a new User on your website', from_email='xiaomei.mandy.li@gmail.com', recipient_list=['tanjajt@gmail.com'])
        return redirect('register')
    else:
       form = UserRegisterForm()
    return render(request, 'Contact/register.html', {'form': form})
