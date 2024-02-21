from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    """
    A form for contacting the website owner.

    This form allows users to send a message to the website owner by providing
    their name, email, and message.

    Attributes:
        name (CharField): The field for the user's name.
        email (EmailField): The field for the user's email address.
        message (CharField): The field for the user's message.

    Methods:
        __init__(self, *args, **kwargs): Initializes the ContactForm instance.
    """

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Send message'))
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['message'].widget.attrs.update({'class': 'form-control',
                                                    'rows': 5})
        self.fields['message'].label = "Your message"
        self.fields['message'].help_text = "Write your message here"
