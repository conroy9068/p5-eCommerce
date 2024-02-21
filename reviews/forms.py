from django import forms
from django.core.exceptions import ValidationError

from .models import Rating


class RatingForm(forms.ModelForm):
    """
    A form for creating or updating a rating.

    This form allows users to select a rating score and provide a comment.

    Attributes:
        RATING_CHOICES (tuple): A tuple of tuples representing
        the rating choices.
        score (ChoiceField): A choice field for selecting the rating score.
        comment (CharField): A text field for providing a comment.

    Methods:
        clean_score: Validates the selected score and raises a
        ValidationError if it is invalid.
    """

    RATING_CHOICES = (
        (0, 'Please select a rating...'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    score = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.Select(
                                attrs={'class': 'custom-select'})
                              )

    class Meta:
        model = Rating
        fields = ['score', 'comment']
        widgets = {
            'comment': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Comment...'}),
        }

    def clean_score(self):
        """
        Validates the selected score.

        Raises:
            ValidationError: If the selected score is invalid.

        Returns:
            str: The selected score.
        """
        score = self.cleaned_data.get('score')
        if int(score) == 0:
            raise ValidationError('Please select a valid score.')
        return score
