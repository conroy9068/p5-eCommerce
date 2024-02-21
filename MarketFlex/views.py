from django.shortcuts import render


def handler404(request, exception):
    """
    Error handler for 404 page not found.

    Args:
        request (HttpRequest): The HTTP request object.
        exception (Exception): The exception that triggered the 404 error.

    Returns:
        HttpResponse: The rendered 404 error page.

    """
    return render(request, 'errors/404.html', status=404)
