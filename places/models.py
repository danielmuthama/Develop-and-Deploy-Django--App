from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.shortcuts import reverse

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model




class park(models.Model):
  id = models.IntegerField(primary_key=True)
  slug = models.CharField(max_length= 100, null=False, blank=True)
  park_name = models.CharField(max_length=50) 
  image = models.ImageField(upload_to ='uploads/')
  description = models.CharField(max_length=300) 

  #the name to display in django admin
  def __str__(self) :
    return str(self.park_name)

class water(models.Model):
  id = models.IntegerField(primary_key=True)
  slug = models.CharField(max_length= 100, null=False, blank=True)
  water_name = models.CharField(max_length=50) 
  image = models.ImageField(upload_to ='uploads/')
  description = models.CharField(max_length=300) 

  #the name to display in django admin
  def __str__(self) :
    return str(self.water_name)

class trail(models.Model):
  id = models.IntegerField(primary_key=True)
  slug = models.CharField(max_length= 100, null=False, blank=True)
  trail_name = models.CharField(max_length=50) 
  image = models.ImageField(upload_to ='uploads/')
  description = models.CharField(max_length=300) 

  #the name to display in django admin
  def __str__(self) :
    return str(self.trail_name)

