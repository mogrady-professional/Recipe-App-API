from django.db import models
# import the abstract base user, base user manager, permissions mixin -> to extend the django user model
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
# Import the manager class -> provides the helper functions for creating a user or superuser
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # extra fields take any extra fields that are passed in and take into extra fields
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields) 
        user.set_password(password) # set the password (encrypted) - important
        user.save(using=self._db) # save the user to the database, supporting multiple databases

        return user
    
    def create_superuser(self, email, password):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

# Create a custom user model
class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager() # Create a custom manager for the user model

    USERNAME_FIELD = 'email' # set the username field to the email field