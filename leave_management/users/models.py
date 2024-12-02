from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('hod', 'HOD'),
        ('staff', 'Staff'),
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='staff')

    def is_hod(self):
        return self.user_type == 'hod'

    def is_staff(self):
        return self.user_type == 'staff'


