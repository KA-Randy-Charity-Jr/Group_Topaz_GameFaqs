from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class GamefaqUser(AbstractUser):
    displayname = models.CharField(max_length=80)
    bio = models.TextField(blank=True, null=True)
    preferred_systems = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.username