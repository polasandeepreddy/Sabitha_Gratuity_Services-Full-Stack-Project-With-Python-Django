from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_message, name='contact_message'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('health/', views.health_check, name='health_check'),
]