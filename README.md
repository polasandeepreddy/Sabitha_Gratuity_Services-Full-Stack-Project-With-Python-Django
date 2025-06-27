# Sabitha Gratuity Services - Django Full Stack Application

A complete Django-based web application for Sabitha Gratuity Services with integrated frontend and backend.

## Features

### Backend (Django + DRF)
- RESTful API with Django Rest Framework
- Contact form handling with email notifications
- Testimonials management system
- Admin panel for content management
- SQLite database (easily configurable for PostgreSQL/MySQL)

### Frontend (Django Templates)
- Modern responsive design with Tailwind CSS
- Professional multi-page website
- Contact form with real-time validation
- Testimonials system with submission form
- Mobile-first responsive design
- Professional animations and micro-interactions

## Quick Start

### Prerequisites
- Python (v3.8 or higher)
- pip (Python package manager)

### Installation & Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

3. **Create Superuser (Optional)**
   ```bash
   python manage.py createsuperuser
   ```

4. **Start Development Server**
   ```bash
   python manage.py runserver
   ```

The application will be available at: http://localhost:8000

## Project Structure

```
├── sgs_backend/           # Django project settings
├── api/                   # API app (REST endpoints)
├── frontend/              # Frontend app (templates & views)
│   ├── templates/         # HTML templates
│   ├── static/           # CSS, JS, images
│   └── views.py          # Frontend views
├── manage.py             # Django management script
└── requirements.txt      # Python dependencies
```

## API Endpoints

- `POST /api/contact/` - Submit contact form
- `GET /api/testimonials/` - Get approved testimonials
- `POST /api/testimonials/` - Submit new testimonial
- `GET /api/health/` - Health check

## Frontend Pages

- `/` - Home page
- `/about/` - About us
- `/services/` - Our services
- `/testimonials/` - Client testimonials
- `/faq/` - Frequently asked questions
- `/contact/` - Contact form

## Admin Panel

Access the Django admin at: http://localhost:8000/admin

Features:
- Manage testimonials
- Approve/reject testimonials
- View submission analytics

## Email Configuration

For production, update the email settings in `sgs_backend/settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'polasandeepreddy0v1@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'  # Add your Gmail app password
```

## Production Deployment

1. **Set DEBUG = False** in settings.py
2. **Configure ALLOWED_HOSTS** in settings.py
3. **Set up proper email backend**
4. **Collect static files**:
   ```bash
   python manage.py collectstatic
   ```
5. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

## Technology Stack

- **Backend**: Django 4.2, Django Rest Framework
- **Frontend**: Django Templates, Tailwind CSS, Vanilla JavaScript
- **Database**: SQLite (default)
- **Icons**: Lucide Icons
- **Styling**: Tailwind CSS (CDN)

## Contact Information

**Sabitha Gratuity Services**
- Phone: +91 90005 52708
- Email: neelima@gratuityservices.com
- Founder: M. Neelima Reddy, FIII
- Service Areas: Telangana, Andhra Pradesh, Karnataka

## License

This project is proprietary software for Sabitha Gratuity Services.# Sabitha_Gratuity_Services-Project-With-Python-Django
# Sabitha_Gratuity_Services-Project-With-Python-Django
