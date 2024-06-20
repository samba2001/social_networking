from django.db import models

# Create your models here.
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone


class CustomModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)
    all_objects = models.Manager()

    class Meta:
        abstract = True


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The User ID must be set')
        user = self.model(userid=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, CustomModel):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12, null=True, blank=True)
    password = models.CharField(max_length=30)
    USERNAME_FIELD = 'email'
    objects = MyUserManager()
