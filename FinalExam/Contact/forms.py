from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField(max_length=50)


    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'password1', 'password2']