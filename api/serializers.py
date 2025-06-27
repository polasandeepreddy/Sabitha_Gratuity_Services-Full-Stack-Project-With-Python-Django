from rest_framework import serializers
from .models import Testimonial


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id', 'name', 'position', 'company', 'location', 'rating', 'text', 'services', 'date', 'created_at']
        read_only_fields = ['id', 'created_at']