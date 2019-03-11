from django.shortcuts import render, redirect 
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile


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
    profile = Profile.objects.all()
    return render(request, 'users/profile.html',{"profile":profile})


    


   