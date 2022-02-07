from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import UserManager


class User(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)    
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default='profiles/default.png', upload_to='profiles')
    about = models.TextField()
    fname = models.CharField(max_length=300)
    lname = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.user.username} Profile'
