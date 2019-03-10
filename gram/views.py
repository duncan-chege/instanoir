from django.shortcuts import render,redirect
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from .models import Image

def home(request):
    imagedata = Image.objects.all()
    title = Noir feed
    return render(request, 'home.html', title=title)

