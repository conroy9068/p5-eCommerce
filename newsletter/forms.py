from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from .models import Subscriber


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super(SubscriberForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Subscribe'))
