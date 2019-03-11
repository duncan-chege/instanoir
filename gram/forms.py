from django import forms
from .models import Image, Comment
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    comment = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'placeholder':'Add a Comment'}))