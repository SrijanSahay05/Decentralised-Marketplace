from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    
    def __str__(self):
        return self.username
    
class UserProfile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    wallet_address = models.CharField(max_length=42, unique=True)
    # profile_pic = models.ImageField(upload_to="media/profile_pics", blank=True)

    def __str__(self):
        return self.user.username
        
