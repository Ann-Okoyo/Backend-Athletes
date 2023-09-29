from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    full_name =models.CharField(max_length=32)
    email = models.EmailField(unique=True)
    password =models.CharField(max_length=33)
    role = models.CharField(max_length=20, default='regular_user')
    
    # REQUIRED_FIELDS= 'email'
       
    

    # USERNAME_FIELD = 'full_name'
    

class Athlete(models.Model):
    full_name =models.CharField(max_length=32)
    email = models.EmailField(unique=True)
    password =models.CharField(max_length=32)
    age = models.PositiveIntegerField()
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='')
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    achievements = models.TextField()
    phone_number = PhoneNumberField(_('Phone Number'), blank=True, null=True)

    role = models.CharField(max_length=20, default='athlete')
    
class Sponsor(models.Model):
    full_name =models.CharField(max_length=32)
    email = models.EmailField(unique=True)
    password =models.CharField(max_length=32)
    Organisation = models.CharField(max_length=255)
    Bio = models.TextField()
    phone_number = PhoneNumberField(_('Phone Number'), blank=True, null=True)

    role = models.CharField(max_length=20, default='sponsor')
