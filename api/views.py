from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .models import Testimonial
from .serializers import TestimonialSerializer


@api_view(['POST'])
def contact_message(request):
    """Handle contact form submissions - Email only, no database storage"""
    
    # Get form data
    name = request.data.get('name', '')
    email = request.data.get('email', '')
    phone = request.data.get('phone', '')
    company = request.data.get('company', '')
    service = request.data.get('service', '')
    message = request.data.get('message', '')
    
    # Basic validation
    if not all([name, email, phone, service, message]):
        return Response({
            'success': False,
            'message': 'Please fill in all required fields.',
            'errors': {'required': 'Name, email, phone, service, and message are required.'}
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # Send email notification
    try:
        subject = f"New Contact Form Submission - {service}"
        email_message = f"""
New contact form submission received:

Name: {name}
Email: {email}
Phone: {phone}
Company: {company}
Service: {service}

Message:
{message}

Please respond to the client directly at: {email}
        """
        
        # Send to the business email
        send_mail(
            subject,
            email_message,
            settings.DEFAULT_FROM_EMAIL,
            ['neelima@gratuityservices.com'],
            fail_silently=False,
        )
        
        # Send confirmation email to the user
        user_subject = "Thank you for contacting Sabitha Gratuity Services"
        user_message = f"""
Dear {name},

Thank you for contacting Sabitha Gratuity Services. We have received your inquiry regarding {service}.

Our team will review your message and get back to you within 24 hours.

Best regards,
Sabitha Gratuity Services Team
M. Neelima Reddy, FIII
Phone: +91 90005 52708
Email: neelima@gratuityservices.com
        """
        
        send_mail(
            user_subject,
            user_message,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=True,
        )
        
        return Response({
            'success': True,
            'message': 'Thank you for your message. We will get back to you within 24 hours.',
            'data': {
                'name': name,
                'email': email,
                'service': service
            }
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        print(f"Email sending failed: {e}")
        return Response({
            'success': False,
            'message': 'Failed to send your message. Please try again or contact us directly.',
            'errors': {'email': 'Email delivery failed'}
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'POST'])
def testimonials(request):
    """Handle testimonials - GET to retrieve, POST to submit"""
    
    if request.method == 'GET':
        # Get approved testimonials only
        testimonials = Testimonial.objects.filter(is_approved=True)
        serializer = TestimonialSerializer(testimonials, many=True)
        return Response({
            'success': True,
            'data': serializer.data
        })
    
    elif request.method == 'POST':
        serializer = TestimonialSerializer(data=request.data)
        
        if serializer.is_valid():
            testimonial = serializer.save()
            
            # Send notification email
            try:
                subject = "New Testimonial Submission"
                message = f"""
New testimonial submitted:

Name: {testimonial.name}
Position: {testimonial.position}
Company: {testimonial.company}
Location: {testimonial.location}
Rating: {testimonial.rating}/5
Services: {', '.join(testimonial.services)}

Testimonial:
{testimonial.text}

Please review and approve in the admin panel.
                """
                
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    ['neelima@gratuityservices.com'],
                    fail_silently=True,
                )
                
            except Exception as e:
                print(f"Email sending failed: {e}")
            
            return Response({
                'success': True,
                'message': 'Thank you for your testimonial! It will be reviewed and published soon.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            'success': False,
            'message': 'Please check your form data and try again.',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def health_check(request):
    """Simple health check endpoint"""
    return Response({
        'status': 'healthy',
        'message': 'Sabitha Gratuity Services API is running'
    })