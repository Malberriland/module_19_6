from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['username']

    def __str__(self):
        return self.email


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

