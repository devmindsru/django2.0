from django.db import models

# Create your models here.

class Users(models.Model):
    firstname = models.CharField(max_length=256)
    lastname = models.CharField(max_length=256)
    email = models.CharField(max_length=256,unique=True)
