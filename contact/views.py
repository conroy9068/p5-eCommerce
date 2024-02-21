from django.conf import settings
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from django.shortcuts import redirect
from django.views.generic import CreateView

from .forms import ContactForm
from .models import Contact


class ContactCreateView(CreateView):
    """
    View for creating a new contact.

    Inherits from CreateView, which provides the functionality for
    creating a new object based on a model and a form.

    Attributes:
        model (Model): The model class that the view will create an
        instance of.
        form_class (Form): The form class that the view will use for data
        validation and rendering.
        template_name (str): The name of the template to be
        used for rendering the view.

    Methods:
        form_valid(form): Overrides the form_valid method of CreateView to
        save the form data, send an email,
        and display success or error messages.
    """
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
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            messages.success(self.request, "Your message has been sent.")
        except BadHeaderError:
            messages.error(self.request, "Invalid header found.")
        except Exception as e:
            # Log the error or send a message to the admin
            messages.error(self.request, f"An error occurred: {e}")
            return redirect('home')

        return redirect('home')
