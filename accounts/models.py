from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
from django.contrib.auth import get_user_model
from datetime import date
from django.core.exceptions import ValidationError
from django.conf import settings
from django.urls import reverse

def validate_dob(value):
        if value> date.today():
            raise ValidationError('Please enter the correct dob!')

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['username']
    objects=CustomUserManager()

    def __str__(self):
        return self.email
    
class Profile(models.Model): 
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='profile')
    date_of_birth=models.DateField(null=True,blank=True,validators=[validate_dob])
    address=models.CharField(null=True,blank=True,max_length=255)
    bio=models.CharField(null=True,blank=True,max_length=500)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    def __str__(self):
        return self.user.email
    
    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk": self.pk})
    

class Follow(models.Model):
    follower = models.ForeignKey('Profile', related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey('Profile', related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')
        indexes = [
            models.Index(fields=['follower', 'following']),
        ]

    def __str__(self):
        return f"{self.follower.user.username} → {self.following.user.username}"
