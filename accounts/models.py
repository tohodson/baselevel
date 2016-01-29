from django.db import models
#from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User
#from django_localflavor_us import models as us_models
# Create your models here.

class User(models.Model):
#class User(AbstractBaseUser):
    """
    Custom user class
    """
    user = models.OneToOneField(User)
    #phone_number = us_models.PhoneNumberField()
    #first_name    = models.CharField(max_length=16)
    #last_name     = models.CharField(max_length=16)

    # contact info
    phone_number  = models.CharField(max_length=12)
    #email         = models.EmailField('email address', unique=True, db_index=True)

    started       = models.DateTimeField()
    is_active     = models.BooleanField(default=True)
    is_admin      = models.BooleanField(default=False)

    class Meta:
        ordering = ('user__last_name', 'user__first_name')

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    @property
    def get_full_name(self):
        return self.user.get_full_name()

    def __str__(self):
        return self.get_full_name()
