from django.shortcuts import render, redirect 
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from gram.models import Image

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')

    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request, id):       #getting specific images posted by one instagrammer
    user = User.objects.get(id=id)      #get specific id of a user
    images=Image.objects.all().filter(grammer_id = user.id)
    return render(request, 'users/profile.html',{'images':images,"user":user})

@login_required
def post(request):          #posting new images for a certain instagrammer
    user = request.user
    if request.method == 'POST':
        newform = NewImageForm(request.POST, request.FILES)
        if newform.is_valid():
            image = newform.save(commit=False)
            image.grammer = user
            image.save()
        return redirect('profile', user.id)
    else:
        newform = NewImageForm()
    return render(request, 'users/newimage.html',{"newform":newform})

@login_required
def specimage(request, id):     #displaying specific images on a separate page
    image = Image.objects.get(id=id)        #get specific id of an image
    print (image)
    return render(request, 'users/specimage.html',{'image':image})
