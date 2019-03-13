from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from gram.models import Image


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

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image_name','image_caption','image_path']
    