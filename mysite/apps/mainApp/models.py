from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    login = models.CharField(max_length = 120)
    nickname = models.TextField() 
    password = models.DateTimeField()
