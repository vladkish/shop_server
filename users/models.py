from django.db import models
from django.contrib.auth.models import AbstractUser

# Main user
class User(AbstractUser):
    image = models.ImageField(upload_to="user_image/")