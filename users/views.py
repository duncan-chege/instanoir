from django.shortcuts import render, redirect 
from .forms import UserRegisterForm, ProfileUpdateForm
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
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)

        if p_form.is_valid():
            p_form.save()
            return redirect ('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'users/profile.html',{'p_form':p_form})


    


   