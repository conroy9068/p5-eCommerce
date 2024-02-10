from django.conf import settings
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from django.shortcuts import redirect
from django.views.generic import CreateView

from .forms import ContactForm
from .models import Contact


class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact/contact_form.html'

    def form_valid(self, form):
        # Save the form first
        self.object = form.save()
        try:
            # Send an email
            send_mail(
                f"Message from {self.object.name}",
                self.object.message,
                settings.EMAIL_HOST_USER,
                fail_silently=False,
            )
            messages.success(self.request, "Your message has been sent.")
            return redirect('home')
        except BadHeaderError:
            messages.error(self.request, "Invalid header found.")
        except Exception as e:
            # Log the error or send a message to the admin
            messages.error(self.request, f"An error occurred: {e}")
