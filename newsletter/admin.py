from django.contrib import admin

from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)
    readonly_fields = ('email',)


admin.site.register(Subscriber, SubscriberAdmin)
