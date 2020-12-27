from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='accounts/profile/', blank=True)
    description = models.TextField(max_length=3000, blank=True, null=True, default='')
