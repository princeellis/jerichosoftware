# Jericho Software Portfolio Site

A modern portfolio website built with Django showcasing projects and work.

## Features

- Home page
- Projects showcase with detailed project pages
- About page
- Privacy Policy page
- Modern dark theme with glassmorphism design
- Responsive layout

## Setup

1. Create a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

2. Install dependencies:
```bash
pip install django
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Run the development server:
```bash
python manage.py runserver
```

## Environment Variables

- `DJANGO_PRODUCTION`: Set to `true` to enable production mode (DEBUG=False)
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts for production

## Projects

- TTP Appointments
- Willo Decisions
- Magic Dining Alerts (Out of service)
- Bible App (Coming soon)
