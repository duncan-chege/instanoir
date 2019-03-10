from django.shortcuts import render,redirect
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from .models import Image

def home(request):
    imagedata = Image.objects.all()
    return render(request, 'home.html',{"imagedata":imagedata})

