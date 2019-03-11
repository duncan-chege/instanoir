from django import forms
from .models import Comment
# from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['username', 'image']
        widgets = {
            'content': forms.TextInput(attrs={'placeholder':'Add a comment'})       #names to be similar as the fieldnames
        }
        