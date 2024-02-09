from djang.contrib import messages
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.shortcuts import render, reverse
from django.urls import reverse_lazy

from .models import Contact


class ContactCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Contact
    fields = ['name', 'email', 'message']
    success_message = "Your message has been sent successfully."

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Your message has been sent.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')