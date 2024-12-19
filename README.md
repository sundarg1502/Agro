# Django E-commerce Website For Agriculture

A fully functional e-commerce website built with Django, HTML, and CSS.

## Features

- User authentication and authorization
- Product catalog with categories
- Shopping cart functionality
- Secure checkout process
- User profiles and order history
- Admin dashboard for product management
- Responsive design for mobile devices

## Prerequisites

- Python 3.8+
- Django 4.0+
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/django-ecommerce.git
cd django-ecommerce
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure environment variables
```bash
cp .env.example .env
# Edit .env file with your settings
```

5. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create superuser
```bash
python manage.py createsuperuser
```

7. Run development server
```bash
python manage.py runserver
```

## Project Structure

```
django-ecommerce/
│
├── manage.py
├── requirements.txt
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── base.html
│   ├── products/
│   ├── cart/
│   └── accounts/
│
└── ecommerce/
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
    └── apps/
        ├── products/
        ├── cart/
        ├── orders/
        └── accounts/
```

## Configuration

### Database Setup
By default, the project uses SQLite. To use PostgreSQL or another database, update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Static Files
Configure your static files settings in `settings.py`:

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

## Usage

1. Access the admin panel at `http://localhost:8000/admin/`
2. Add products and categories through the admin interface
3. Visit `http://localhost:8000` to view the store
4. Register user accounts to test shopping functionality

## Development

### Adding New Features
1. Create a new app: `python manage.py startapp new_feature`
2. Add the app to `INSTALLED_APPS` in `settings.py`
3. Create models, views, and templates
4. Add URL patterns in `urls.py`

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Comment complex logic
- Write tests for new features

## Testing

Run tests with:
```bash
python manage.py test
```

## Deployment

1. Set `DEBUG = False` in production
2. Configure proper database settings
3. Set up static file serving
4. Use environment variables for sensitive data
5. Configure HTTPS
6. Set up proper security headers

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Create a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

- Your Name
- Email: your.email@example.com
- GitHub: [@yourusername](https://github.com/yourusername)

## Acknowledgments

- Django documentation
- Bootstrap for UI components
- Font Awesome for icons


## Demo Screenshots

### Homepage
![Homepage Screenshot](/screenshots/homepage.png)
*Homepage featuring product categories, featured items, and navigation*

### Product Catalog
![Product Catalog](/screenshots/product-catalog.png)
*Product listing page with filters and search functionality*

### Product Detail
![Product Detail](/screenshots/product-detail.png)
*Detailed product view with images, description, and add to cart option*

### Shopping Cart
![Shopping Cart](/screenshots/shopping-cart.png)
*Shopping cart with product quantities and checkout options*

### Checkout Process
![Checkout Process](/screenshots/checkout.png)
*Secure checkout page with shipping and payment details*

### Admin Dashboard
![Admin Dashboard](/screenshots/admin-dashboard.png)
*Administrative interface for managing products, orders, and users*

### Mobile Responsive Design
![Mobile View](/screenshots/mobile-view.png)
*Mobile-friendly interface showing responsive design*

