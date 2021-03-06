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
        name= form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')

        data = {
            'name':name,
            'username': username,
            'email':email
        }

        message = '''
        New user signed up to our website. 
        Name {}
        User {}
        Email {}
        '''. format(data['name'],data['username'],data['email'])

        send_mail(subject='New User', message = message, from_email='', recipient_list=['xiaomei.mandy.li@gmail.com'])
        return redirect('register')
    else:
       form = UserRegisterForm()
    return render(request, 'Contact/register.html', {'form': form})
