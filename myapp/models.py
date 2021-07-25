from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class MyUser(AbstractUser):
    mobile_number = PhoneNumberField(max_length=10, unique=True, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    facebook_id = models.CharField(max_length=255, null=True, blank=True)
    google_id = models.CharField(max_length=255, null=True, blank=True)
