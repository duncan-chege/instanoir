from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ProfileUpdateForm(forms.ModelForm):      #create a form that'll update our user model
    bio = forms.CharField()

    class Meta:
        model = Profile
        fields = ['bio','image']
