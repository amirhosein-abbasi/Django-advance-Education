from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser, PermissionsMixin)
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver



class UserManager(BaseUserManager):
    '''
    custom user manager where email is the unique identifires for authentication instead of usernames.
    '''
    def create_user(self,email,password,**extra_fields):
        '''
        create user with the given email and password and extra data.
        '''
        if not email:
            raise ValueError(_('The Email must be set dayi jan'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,password,**extra_fields):
        '''
        create super user
        '''
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('bayad true bashe vase super user'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('inam bayad true bashe vase super user'))

        return self.create_user(email,password,**extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    '''
    custom user model for our app
    '''
    email = models.EmailField(max_length=255,unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    #is_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=250)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email


@receiver(post_save,sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)