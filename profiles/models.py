from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    Represents a user profile in the system.

    Attributes:
        user (User): The associated user for this profile.
        default_phone_number (str): The default phone number for the user.
        default_street_address1 (str): The first line of the default street
        address for the user.
        default_street_address2 (str): The second line of the default street
        address for the user.
        default_town_or_city (str): The default town or city for the user.
        default_county (str): The default county for the user.
        default_postcode (str): The default postcode for the user.
        default_country (Country): The default country for the user.

    Methods:
        __str__(): Returns the username of the associated user.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True,
                                            blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True,
                                               blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True,
                                               blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True,
                                            blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True,
                                   blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile

    This function is a signal receiver that is triggered whenever a
    User object is saved.
    It creates or updates the corresponding UserProfile object for the user.

    Parameters:
    - sender: The model class that sent the signal (User in this case)
    - instance: The actual instance of the model that was saved (User instance)
    - created: A boolean indicating whether the User object was created
    or updated
    - kwargs: Additional keyword arguments

    Returns:
    None
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
