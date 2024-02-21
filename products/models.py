from django.db import models


class Category(models.Model):
    """
    Represents a category for products.
    """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Represents a product in the eCommerce system.

    Attributes:
        category (Category): The category that the product belongs to.
        sku (str): The stock keeping unit (SKU) of the product.
        name (str): The name of the product.
        description (str): The description of the product.
        has_sizes (bool): Indicates whether the product has different sizes.
        price (Decimal): The price of the product.
        image_url (str): The URL of the product image.
        image (ImageField): The image file of the product.

    Methods:
        __str__(): Returns a string representation of the product.
    """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
