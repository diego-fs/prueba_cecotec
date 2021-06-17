#Third party imports
from django.db import models
##Module imports
from random import randint


class User(models.Model):

    username = models.CharField(max_length=80, unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(verbose_name="Address", max_length=255, unique=True)
    password = models.CharField(verbose_name="Password", max_length=128)
    
    class Meta:
        app_label = "users"
        
    def get_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.get_name()
    
    def generate_random_password(self):
        password = ""
        allowed_chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        for i in range(0,9):
            char = allowed_chars[randint(0, len(allowed_chars))]
            password = password.join(char)
        return password