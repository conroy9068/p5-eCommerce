from django.contrib import messages
from django.shortcuts import redirect, render, reverse

from .forms import OrderForm

# Create your views here.


def checkout(request):
    """ A view to return the checkout page """

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OYWOmF6Vc5JVoWZkc4OnevOTWvNEoy4fjzCd628fn394ja913tjMyfu8KgLWGFsZtXPeHGw0fipTKsJdEieZCDa00iEi4vtb4',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)