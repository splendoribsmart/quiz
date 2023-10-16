from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=120)
    region = models.CharField(max_length=120, blank=True, null=True)

    # Add related_name to avoid clashes
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')

# Additional fields can be added here
