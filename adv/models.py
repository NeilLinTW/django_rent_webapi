# from datetime import datetime
from django.db import models
from users.models import User

# Create your models here.

class Advertisement(models.Model):
    Id = models.AutoField(primary_key=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    City = models.CharField(max_length=8)
    Town = models.CharField(max_length=10)
    Addr = models.CharField(max_length=50)
    Body = models.CharField(max_length=500)
    IP = models.CharField(max_length=50,null = True,blank=True)
    IsEnable = models.BooleanField(default=False)
    IsPay = models.BooleanField(default=False)
    Image1 = models.CharField(max_length=200,default='')
    Image2 = models.CharField(max_length=200,null = True)
    CreateDate = models.DateTimeField(auto_now_add=True)
    ModifyDate = models.DateTimeField(null = True,blank=True)
    
    class Meta:
            db_table = 'Advertisement'

            

class RateHistory(models.Model):
    Id = models.AutoField(primary_key=True)
    IPAddr = models.CharField(max_length=50)
    Val = models.SmallIntegerField(default=0)
    CreateDate = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = 'RateHistory'