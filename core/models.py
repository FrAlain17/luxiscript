from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    # Add more fields as needed, e.g., subscription status
    
    def __str__(self):
        return self.email
