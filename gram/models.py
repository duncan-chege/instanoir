from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    image_name = models.CharField(max_length=100)
    image_caption = models.CharField(max_length=200)          
    image_path = models.ImageField(upload_to = 'photos/')
    like = models.IntegerField(default=0)
    comment = models.TextField(null=True, blank=True)
    grammer = models.ForeignKey(User, on_delete=models.CASCADE)     #models.CASCADE-if a user is deleted, delete their posts as well

    def __str__(self):
        return self.image_name      #how it'll be printed on shell