from django.db import models

class User(models.Model):
    # Define your fields here
    username = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
