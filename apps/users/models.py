from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, default='')
    verified = models.BooleanField(default=False)
    city = models.ForeignKey('core.City', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.username
