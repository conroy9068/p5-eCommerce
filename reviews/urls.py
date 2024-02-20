from django.urls import path


from .views import rate_product

urlpatterns = [
    # ... your other url patterns ...
    path('product/<int:product_id>/rate/', rate_product, name='rate_product'),
]
