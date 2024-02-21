from django.db import models
from django.shortcuts import reverse
from django.utils import timezone


class Contact(models.Model):
    """
    Represents a contact in the system.

    Attributes:
        name (str): The name of the contact.
        email (str): The email address of the contact.
        message (str): The message sent by the contact.
        created_at (datetime): The date and time when the contact was created.
    """

    class Meta:
        verbose_name_plural = 'Contacts'

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')