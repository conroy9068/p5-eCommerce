from django.shortcuts import render


def index(request):
    """
    A view that displays the index page.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - The rendered index.html template.
    """
    return render(request, 'home/index.html')


def about(request):
    """
    A view that displays the about page.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - The rendered about page.
    """
    return render(request, 'home/about.html')
