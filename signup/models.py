from django.db import models

# Create your models here.

# user model

class UserModel(models.Model):
    first_name = models.CharField(max_length=20,default='')
    last_name = models.CharField(max_length=20,default='')
    course = models.CharField(max_length=20,default='')
    regno = models.CharField(max_length=10,default='')
    email = models.CharField(max_length=100,default='')
    phone = models.CharField(max_length=10,default='')
    
    