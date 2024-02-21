from django.contrib import admin

from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    """
    Admin class for managing products.

    This class defines the configuration for the admin interface
    of the Product model.
    """

    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Admin class for managing categories.

    This class defines the configuration for the admin interface.
    """
    list_display = (
        'friendly_name',
        'name',
        )


"""
Register the Product and Category models with the admin interface.
"""
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)