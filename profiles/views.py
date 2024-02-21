from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from checkout.models import Order

from .forms import UserProfileForm
from .models import UserProfile

# Create your views here.


@login_required
def profile(request):
    """
    Display the user's profile.

    This view function is responsible for rendering the user's profile page.
    It retrieves the UserProfile object associated with the currently
    authenticated user and displays it along with a form to update the profile
    information. If the request method is POST, it processes the form data and
    updates the profile if the form is valid. Otherwise, it simply
    renders the profile page with the existing profile information.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A rendered HTML template displaying the user's profile page.

    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure the form is valid.')
                           )
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """
    View function to display the order history for a specific order number.

    Args:
        request (HttpRequest): The HTTP request object.
        order_number (str): The order number.

    Returns:
        HttpResponse: The HTTP response object containing the rendered
        template.
    """
    order = get_object_or_404(Order, order_number=order_number)

    if order.user_profile.user != request.user:
        messages.error(request, "You don't have permission to view this order")
        return redirect(reverse('products'))

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
