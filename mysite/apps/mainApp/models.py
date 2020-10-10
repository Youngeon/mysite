from django.db import models

class Users(models.Model):
    login = models.CharField(max_length = 120)
    nickname = models.TextField() 
    password = models.DateTimeField()
