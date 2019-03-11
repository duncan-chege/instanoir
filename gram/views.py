from django.shortcuts import render,redirect
# from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User     # user class
from .models import Image,Comment
from .forms import CommentForm

def home(request):
    imagedata = Image.objects.all().order_by('-id')
    # comments = Comment.objects.all()
    return render(request, 'home.html',{"imagedata":imagedata})

