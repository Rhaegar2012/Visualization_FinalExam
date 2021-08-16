
from django.contrib import admin
from django.urls import path
from Contact import views


urlpatterns = [
    path('admin/', admin.site.urls, name='Contact'),
    path('', views.register, name="register")

]
