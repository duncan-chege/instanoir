from django.shortcuts import render,redirect
# from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User     # user class
from .models import Image,Comment
from .forms import CommentForm

def home(request):
    imagedata = Image.objects.all().order_by('-id')     #arranging images from most recent as the first to be seen
    comments = Comment.objects.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            image_id = int(request.POST.get('comment_id'))     #get the id of the name of a comment input field for a specific post. The id of input field is in string, so i convert it into int
            image = Image.objects.get(id = image_id)        #get the id of a specific image and associate it with its specific comment field
            comment = comment_form.save()
            comment.username = request.user
            comment.image = image
            comment.save()      #saving a comment
        return redirect('home')
    else:
        comment_form = CommentForm()

    print(comments)
    return render(request, 'home.html',{"imagedata":imagedata, "comments": comments, "comment_form":comment_form})

