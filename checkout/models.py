import uuid

from django.conf import settings
from django.db import models
from django.db.models import Sum
from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile

# Create your models here.


class Order(models.Model):
    """
    Represents an order made by a user in the eCommerce system.

    Attributes:
        order_number (str): The unique order number.
        user_profile (UserProfile): The user profile associated with the order.
        full_name (str): The full name of the user placing the order.
        email (str): The email address of the user placing the order.
        phone_number (str): The phone number of the user placing the order.
        country (Country): The country of the user placing the order.
        postcode (str): The postcode of the user placing the order.
        town_or_city (str): The town or city of the user placing the order.
        street_address1 (str): The first line of the street address of the
        user placing the order.
        street_address2 (str): The second line of the street address of the
        user placing the order.
        county (str): The county of the user placing the order.
        date (datetime): The date and time when the order was created.
        delivery_cost (Decimal): The cost of delivery for the order.
        order_total (Decimal): The total cost of the order.
        grand_total (Decimal): The grand total cost of the order,
        including delivery.
        original_bag (str): The original bag contents of the order.
        stripe_pid (str): The Stripe payment ID associated with the order.

    Methods:
        _generate_order_number(): Generates a random, unique order
        number using UUID.
        update_total(): Updates the grand total of the order each time
        a line item is added.
        save(*args, **kwargs): Overrides the original save method to set
        the order number.
        __str__(): Returns the order number as a string representation of
        the order.
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True,
                                     blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID.
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added.
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum']
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = (self.order_total *
                                  settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    Represents a line item in an order.

    Attributes:
        order (Order): The order to which this line item belongs.
        product (Product): The product associated with this line item.
        product_size (str): The size of the product (optional).
        quantity (int): The quantity of the product in this line item.
        lineitem_total (Decimal): The total cost of this line item.

    Methods:
        save(*args, **kwargs): Override the original save method to set the
        line item total.
        __str__(): Returns a string representation of the line item.
    """
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    product_size = models.CharField(max_length=20, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'