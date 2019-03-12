from django.shortcuts import render, redirect 
from .forms import UserRegisterForm, ProfileUpdateForm
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
def profile(request):
    images = Image.objects.filter(upload_by = user)
    return render(request, 'users/profile.html',{'images':images})

@login_required
def update(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)

        if p_form.is_valid():
            p_form.save()
            return redirect ('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'users/update.html',{'p_form':p_form})







   