from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser

class AppUserManager(BaseUserManager):
    def create_user(self, email, password, username, first_name, last_name, phone, gender, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        if not password:
            raise ValueError('Password is required')
        if not username:
            raise ValueError('Username is required')
        if not first_name:
            raise ValueError('First name is required')
        if not last_name:
            raise ValueError('Last name is required')
        if not phone:
            raise ValueError('Phone is required')
        if not gender:
            raise ValueError('Gender is required')
        
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            phone = phone,
            gender= gender,
            **extra_fields

        )

        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password = None):
        if not email:
            raise ValueError('Email is required')
        if not password:
            raise ValueError('Password is required')
        
        user = self.model(
            email = self.normalize_email(email),
            password = password,
            is_staff = True,
            is_superuser = True
        )
        user.save()
        return user