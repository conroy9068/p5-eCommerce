from django.urls import path

from .views import ContactCreateView

urlpatterns = [
    path('contact_us/', ContactCreateView.as_view(), name='contact_us'),
]
