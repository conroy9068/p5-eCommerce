from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from products.models import Product

from .forms import RatingForm


@login_required
def rate_product(request, product_id):
    """
    View function to rate a product.

    Args:
        request (HttpRequest): The HTTP request object.
        product_id (int): The ID of the product to be rated.

    Returns:
        HttpResponse: The HTTP response object.

    Raises:
        Http404: If the product with the given ID does not exist.
    """
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.product = product
            rating.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = RatingForm()

    return render(request, 'product/rate_product.html', {'form': form,
                                                         'product': product})
