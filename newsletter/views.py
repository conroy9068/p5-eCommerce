from django.conf import settings
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from .forms import SubscriberForm


def subscribe(request):
    """
    View function for subscribing to the newsletter.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.

    Raises:
        None
    """
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            # Debugging: Print the cleaned data
            print("Cleaned data:", form.cleaned_data['email'])
            subscriber = form.save()
            messages.success(request, 'You have successfully subscribed.')
            send_confirmation_email(request, subscriber.email)
            return redirect('home')
    else:
        form = SubscriberForm()
    return render(request, 'newsletter/subscribe.html', {'form': form})


def send_confirmation_email(request, email):
    """
    Send the user a confirmation email.

    Args:
        request (HttpRequest): The HTTP request object.
        email (str): The email address of the user.

    Raises:
        BadHeaderError: If an invalid header is found.
        Exception: If any other error occurs.

    Returns:
        None
    """
    try:
        subject = render_to_string(
            'newsletter/confirmation_emails/confirmation_email_subject.txt',
            {'email': email}
        ).strip()
        body = render_to_string(
            'newsletter/confirmation_emails/confirmation_email_body.txt',
            {'email': email, 'contact_email': settings.EMAIL_HOST_USER}
        )

        send_mail(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            [email]
        )
    except BadHeaderError:
        messages.error(request, "Invalid header found.")
    except Exception as e:
        messages.error(request, f"An error occurred: {e}")
