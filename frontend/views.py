from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from api.models import Testimonial
from api.serializers import TestimonialSerializer
from api.views import contact_message, testimonials as api_testimonials


def home(request):
    return render(request, 'frontend/home.html')


def about(request):
    return render(request, 'frontend/about.html')


def services(request):
    return render(request, 'frontend/services.html')


def testimonials(request):
    return render(request, 'frontend/testimonials.html')


def faq(request):
    return render(request, 'frontend/faq.html')


def contact(request):
    return render(request, 'frontend/contact.html')