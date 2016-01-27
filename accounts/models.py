from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class User(AbstractBaseUser):
    """
    Custom user class
    """
    first_name    = models.CharField(max_length=16)
    last_name     = models.CharField(max_length=16)

    # contact info
    phone_number  = models.CharField(max_length=12)
    email         = models.EmailField('email address', unique=True, db_index=True)

    started       = models.DateTimeField()
    is_active     = models.BooleanField(default=True)
    is_admin      = models.BooleanField(default=False)


    def __str__(self):
        return str(self.first_name) + str(self.last_name)
