from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, phone_number, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        if not phone_number:
            raise ValueError('Users must have a phone number')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, phone_number=phone_number)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, name, phone_number, password):
        user = self.create_user(email, name, phone_number, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=120, unique=True)
    name = models.CharField(max_length=60, blank=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='media/profile_pics/', blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone_number']

    def __str__(self):
        return self.name