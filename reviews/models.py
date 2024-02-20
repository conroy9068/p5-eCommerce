from django.conf import settings
from django.db import models


class Rating(models.Model):
    # Link to the User model (assuming you're using Django's built-in User model)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Link to the Product model
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    # The actual rating, could be a number from 1 to 5 for example
    score = models.PositiveSmallIntegerField()
    # Optionally, you can include a comment with the rating
    comment = models.TextField(null=True, blank=True)
    # Timestamps for the rating
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Rating {self.score} for {self.product.name} by {self.user.username}'
