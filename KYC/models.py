from django.db import models

# Create your models here.

class KYC(models.Model):
    email = models.CharField(max_length=255) 
    name = models.CharField(max_length=255)
    aadhar_number = models.CharField(max_length=20)
    pan_number = models.CharField(max_length=20)
    aadhar_photo = models.ImageField(upload_to='aadhar_images/')

class Profile(models.Model):
    
    pic=models.ImageField(upload_to='images/' )