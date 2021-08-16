from django.contrib import admin
from django.urls import path
from Contact import views


urlpatterns = [
    path('', views.contactView, name='Contact')
]
