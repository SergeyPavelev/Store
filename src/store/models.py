from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """Custom user model"""
    phone = models.CharField(max_length=14, unique=True)
    
    def __str__(self) -> str:
        return f'{self.username}'
