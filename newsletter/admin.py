from django.contrib import admin

from .models import Subscriber


# Define an admin class if you want to customize the admin interface
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email',)  # Show email field in the list display
    search_fields = ('email',)  # Allow searching by email
    readonly_fields = ('email',)  # Make email field read-only if needed

# Register the admin class with the associated model
admin.site.register(Subscriber, SubscriberAdmin)
