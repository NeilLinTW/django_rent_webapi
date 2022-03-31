from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth.models import BaseUserManager , AbstractBaseUser , PermissionsMixin
from django.utils import timezone
from datetime import datetime

# Create your models here.

class UserManager(BaseUserManager):
    def _createuser(self , username , email , password , is_active , is_staff , is_superuser , **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError("username錯誤")

        email = self.normalize_email(email)
        user = self.model(username = username , email = email , is_active = is_active , 
            is_staff = is_staff , is_superuser = is_superuser , date_joined = now , **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def createuser(self , username , email , password, **extra_fields):
        return self._createuser(username , email , password,
            is_active=True, is_staff=False, is_superuser=False)

    def create_superuser(self ,  username , email , password, **extra_fields):
        user = self._createuser(username , email , password,is_active=True, is_staff=True, is_superuser=True, **extra_fields)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser , PermissionsMixin):
    first_name = None
    last_name = None
    
    username = models.CharField(max_length=30,unique=True)
    email = models.CharField(max_length=50,unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=datetime.now())

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

