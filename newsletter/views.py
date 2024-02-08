from django.conf import settings
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from .forms import SubscriberForm


def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            # Debugging: Print the cleaned data
            print("Cleaned data:", form.cleaned_data['email'])
            subscriber = form.save()
            messages.success(request, 'You have successfully subscribed.')
            send_confirmation_email(request, form.cleaned_data['email'])
            return redirect('home')
    else:
        form = SubscriberForm()
    return render(request, 'newsletter/subscribe.html', {'form': form})



def send_confirmation_email(request, email):
    """Send the user a confirmation email."""
    try:
        subject = render_to_string(
            'newsletter/confirmation_emails/confirmation_email_subject.txt',
            {'email': email}
        ).strip()  # Remove any leading/trailing whitespace
        body = render_to_string(
            'newsletter/confirmation_emails/confirmation_email_body.txt',
            {'email': email, 'contact_email': settings.DEFAULT_FROM_EMAIL}
        )
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [email]
        )
    except BadHeaderError:
        messages.error(request, "Invalid header found.")
    except Exception as e:
        messages.error(request, f"An error occurred: {e}")
