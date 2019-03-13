from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)     #one to one relationsip gives user ablity to access the profile directly from the user
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio =  models.CharField(max_length=100,default='No bio available')         

    def __str__(self):
        return f"{self.user.username}'s Profile" 

    

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
    @classmethod
    def search_username_profile(cls,search_term):
        userz = cls.objects.filter(user__username__icontains=search_term)
        return userz