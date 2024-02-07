from django.conf import settings
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SubscriberForm
from .models import Subscriber


def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully subscribed.')
            return redirect('home')
    else:
        form = SubscriberForm()
    return render(request, 'newsletter/subscribe.html', {'form': form})


class MailingListCreateView(CreateView):
    model = Subscriber
    fields = ['email']
    template_name = 'newsletter/subscribe.html'
    success_url = reverse_lazy('success_url')


def _send_confirmation_email(self, order):
    """Send the user a confirmation email."""
    cust_email = order.email
    try:
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order}
        ).strip()  # Remove any leading/trailing whitespace
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
        )
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )
    except BadHeaderError:
        # Handle the exception if the email has a bad header
        print("Invalid header found.")
    except Exception as e:
        # Catch all other exceptions and print them
        print(f"An error occurred: {e}")


def form_valid(self, form):
    self.object = form.save()
    messages.success(
        self.request,
        "Thanks for subscribing to our newsletter!"
    )
    self._send_confirmation_email(self.object.email)
    return super().form_valid(form)