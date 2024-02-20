from django import forms
from django.core.exceptions import ValidationError

from .models import Rating


class RatingForm(forms.ModelForm):
    # Define a tuple of tuples with the rating choices
    RATING_CHOICES = (
        (0, 'Please select a rating...'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    # Override the score field to use the choices
    score = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.Select(attrs={'class': 'custom-select'}))

    class Meta:
        model = Rating
        fields = ['score', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your comment...'}),
        }

    def clean_score(self):
        score = self.cleaned_data.get('score')
        if int(score) == 0:  # Convert score to integer before comparison
            raise ValidationError('Please select a valid score.')
        return score

