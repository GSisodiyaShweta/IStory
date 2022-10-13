from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User


# Create your models here.

class Player(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    your_name = models.CharField(max_length=200)

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author is a string rather than an object because it hasn't been declared yet in the file
    your_email = models.EmailField(max_length=200)

    player_s_choices = models.TextField(max_length=1000)

    def __str__(self):
        """String for representing the Model object."""
        return self.your_name
