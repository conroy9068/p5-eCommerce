from django import forms

from .models import Category, Product
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    """
    A form for creating or updating a product.

    Inherits from forms.ModelForm and provides additional functionality
    for handling product data.

    Attributes:
        image (forms.ImageField): An optional image field for the product.
        category (forms.ChoiceField): A field for selecting the category
        of the product.

    Methods:
        __init__(self, *args, **kwargs): Initializes the form and sets
        the choices for the category field.

    """

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        # List comprehension to create friendly names for categories
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # Update category field on form to use friendly names
        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
