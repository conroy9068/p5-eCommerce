from django.conf import settings
from django.db import models


class Rating(models.Model):
    """
    Represents a rating given by a user for a product.

    Attributes:
        user (ForeignKey): The user who gave the rating.
        product (ForeignKey): The product being rated.
        score (PositiveSmallIntegerField): The score given by the user.
        comment (TextField): An optional comment provided by the user.
        created_at (DateTimeField): The date and time when the
        rating was created.
        updated_at (DateTimeField): The date and time when the
        rating was last updated.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField()
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return (
            f'Rating {self.score} for {self.product.name} '
            f'by {self.user.username}'
        )
