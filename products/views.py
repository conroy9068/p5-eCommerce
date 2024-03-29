from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Q
from django.db.models.functions import Lower
from django.shortcuts import get_object_or_404, redirect, render, reverse

from reviews.forms import RatingForm

from .forms import ProductForm
from .models import Category, Product


def all_products(request):
    """
    A view to show all products, including sorting and search queries.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered
        template.
    """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    products = Product.objects.annotate(average_rating=Avg('rating__score'))

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    View function that displays the details of a product.

    Args:
        request (HttpRequest): The HTTP request object.
        product_id (int): The ID of the product.

    Returns:
        HttpResponse: The HTTP response object containing the
        rendered template.
    """
    product = get_object_or_404(Product, pk=product_id)
    ratings = product.rating_set.all()
    rating_form = RatingForm()
    average_rating = ratings.aggregate(Avg('score'))['score__avg'] or 0
    average_rating = round(average_rating, 1)

    # Set a variable to check if the user has already reviewed the product
    user_has_reviewed = False

    # Check if the user has already submitted a rating
    if request.user.is_authenticated:
        # Check if the user has already submitted a rating
        user_has_reviewed = ratings.filter(user=request.user).exists()

    if request.method == 'POST' and 'rating_submit' in request.POST:
        # Check if the user has not reviewed yet before processing the form
        if not user_has_reviewed:
            rating_form = RatingForm(request.POST)
            if rating_form.is_valid():
                rating = rating_form.save(commit=False)
                rating.user = request.user
                rating.product = product
                rating.save()
                return redirect('product_detail', product_id=product.id)
        else:
            messages.error(request, 'You have already reviewed this product.')
            pass

    context = {
        'product': product,
        'ratings': ratings,
        'rating_form': rating_form if not user_has_reviewed else None,
        'average_rating': average_rating,
        'user_has_reviewed': user_has_reviewed,
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    Add a product to the store.

    This function is responsible for adding a product to the store.
    Only store owners (superusers) are allowed to perform this action.
    The function handles both GET and POST requests.
    If the request method is POST, the function validates the form data
    and saves the product to the database. If the form is valid,
    a success message is displayed and the user is redirected to the
    product detail page. If the form is invalid, an error message is
    displayed. If the request method is GET, an empty form
    is rendered.

    Args:
    - request: The HTTP request object.

    Returns:
    - If the request method is POST and the form is valid, the function
    redirects the user to the product detail page.
    - If the request method is POST and the form is invalid, the function
    renders the add_product.html template with the form and error message.
    - If the request method is GET, the function renders the
    add_product.html template with an empty form.

    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
            'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the store.

    Args:
        request (HttpRequest): The HTTP request object.
        product_id (int): The ID of the product to be edited.

    Returns:
        HttpResponse: The HTTP response object.

    Raises:
        Http404: If the product with the given ID does not exist.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {product.name}')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           f'Failed to update {product.name}. '
                           f'Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product from the store.

    Args:
        request (HttpRequest): The HTTP request object.
        product_id (int): The ID of the product to be deleted.

    Returns:
        HttpResponseRedirect: A redirect response to the products page.

    Raises:
        Http404: If the product with the given ID does not exist.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
