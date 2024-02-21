from django.contrib import admin

from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    """
    Admin class for managing subscribers.

    Attributes:
        list_display (tuple): Fields to display in the admin list view.
        search_fields (tuple): Fields to enable search functionality
        in the admin.
        readonly_fields (tuple): Fields that are read-only in the admin.
    """
    list_display = ('email',)
    search_fields = ('email',)
    readonly_fields = ('email',)


admin.site.register(Subscriber, SubscriberAdmin)
