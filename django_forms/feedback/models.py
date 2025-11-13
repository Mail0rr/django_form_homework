from django.conf.global_settings import EMAIL_HOST
from django.db import models
from django.db.models import TextField
from django.forms import CharField, EmailField, DateTimeField
from django.contrib.auth.models import AbstractUser


class Feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} -> {self.email}"

