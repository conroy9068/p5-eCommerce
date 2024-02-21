from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from .models import Subscriber


class SubscriberForm(forms.ModelForm):
    """
    A form for subscribing to the newsletter.

    This form is used to collect the email address of a subscriber.

    Attributes:
        email (CharField): The field for entering the email address.

    Methods:
        __init__(self, *args, **kwargs): Initializes the form.
    """
    class Meta:
        model = Subscriber
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super(SubscriberForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Subscribe'))
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
