from django.db import models
from django.shortcuts import reverse


class Subscriber(models.Model):
    """
    Represents a subscriber to the newsletter.

    Attributes:
        email (str): The email address of the subscriber.

    Methods:
        __str__(): Returns a string representation of the subscriber's
        email address.
        get_absolute_url(): Returns the URL for the home page.
    """
    class Meta:
        verbose_name_plural = 'Email Addresses'

    email = models.EmailField(
        max_length=254,
        unique=True,
        error_messages={'unique': "This email is already subscribed."}
        )

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('home')
