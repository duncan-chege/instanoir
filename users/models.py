from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)     #one to one relationsip gives user ablity to access the profile directly from the user
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio =  models.CharField(max_length=100,default='No bio available')         

    def __str__(self):
        return f"{self.user.username}'s Profile" 