from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ContactForm
from .models import Contact


class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact/contact_form.html'
    success_url = reverse_lazy('home')  # Update with your actual success URL
    success_message = "Your message has been sent successfully."

    def form_valid(self, form):
        # Save the form first
        self.object = form.save()
        # Send an email
        send_mail(
            f"Message from {self.object.name}",
            self.object.message,
            self.object.email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        messages.success(self.request, self.success_message)
        return redirect(self.success_url)
