from django.db import models
from django.shortcuts import reverse
from django.utils import timezone


class Contact(models.Model):
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