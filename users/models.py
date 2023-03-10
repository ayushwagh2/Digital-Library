from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from blog.models import Document2

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    StudentID = models.PositiveIntegerField()
     
    def __str__(self):
        return self.user.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    Stream = models.CharField(max_length=100)
 

    def __str__(self):
        return f'{self.user.username} Profile'

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

