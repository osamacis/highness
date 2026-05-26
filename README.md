# Highness - Premium Cerelac E-Commerce Platform

A modern, parent-focused e-commerce platform for premium cerelac and millet-based baby food products. Built with Django and featuring a beautiful, responsive design optimized for converting parents into customers.

## 🎯 Features

### Core Features
- **Product Catalog** - Browse products by category and age group
- **Smart Filtering** - Filter by age, category, price, and more
- **Product Details** - Comprehensive product information with nutritional data
- **Shopping Cart** - Add products to cart (ready for checkout integration)
- **Search** - Full-text search across products
- **Responsive Design** - Mobile-first approach, works on all devices

### Content Management
- **Blog Section** - Parenting tips and nutrition articles
- **Recipe Collection** - Age-appropriate recipes using Highness products
- **About Page** - Brand story and founder information
- **Contact Page** - Customer support and inquiry form
- **Newsletter** - Email subscription for updates and offers

### Parent-Focused Features
- **Trust Badges** - Safety certifications and quality indicators
- **Testimonials** - Real parent reviews and experiences
- **Age-Based Recommendations** - Products tailored to child's age
- **Nutritional Information** - Detailed ingredient and nutrition facts
- **Safety Certifications** - Display of quality and safety standards

### Design & UX
- **Modern Aesthetic** - Premium gradient design with indigo/pink/amber palette
- **Smooth Animations** - Micro-interactions and scroll effects
- **Glassmorphism** - Modern glass effect UI elements
- **Professional Typography** - Poppins headings, Inter body text
- **Accessibility** - WCAG compliant with focus indicators

## 🛠️ Tech Stack

- **Backend**: Django 4.x
- **Frontend**: Bootstrap 5, Custom CSS3
- **Database**: SQLite (development), PostgreSQL (production-ready)
- **Styling**: Modern CSS with gradients and animations
- **Icons**: Bootstrap Icons
- **Fonts**: Google Fonts (Poppins, Inter)

## 📋 Requirements

- Python 3.8+
- Django 4.0+
- pip (Python package manager)

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/highness.git
cd highness
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment
Create a `.env` file in the project root:
```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Load Sample Data (Optional)
```bash
python manage.py seed_data
```

### 8. Run Development Server
```bash
python manage.py runserver
```

Visit `http://localhost:8000` in your browser.

## 📁 Project Structure

```
highness/
├── blog/                    # Blog and recipe management
│   ├── models.py           # Blog post and recipe models
│   ├── views.py            # Blog views
│   └── urls.py             # Blog URL routing
├── products/               # Product catalog
│   ├── models.py           # Product, category, age group models
│   ├── views.py            # Product views
│   └── urls.py             # Product URL routing
├── pages/                  # Static pages
│   ├── models.py           # Contact form model
│   ├── views.py            # Page views
│   └── urls.py             # Page URL routing
├── core/                   # Core functionality
│   ├── models.py           # Core models (USP, testimonials)
│   ├── context_processors.py # Global context data
│   └── templatetags/       # Custom template tags
├── templates/              # HTML templates
│   ├── base.html           # Base template
│   ├── includes/           # Reusable components
│   ├── pages/              # Page templates
│   ├── products/           # Product templates
│   └── blog/               # Blog templates
├── static/                 # Static files
│   ├── css/                # Stylesheets
│   └── js/                 # JavaScript files
├── media/                  # User-uploaded files
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── .gitignore             # Git ignore rules
```

## 🎨 Design System

### Color Palette
- **Primary**: #6366F1 (Indigo)
- **Secondary**: #EC4899 (Pink)
- **Accent**: #F59E0B (Amber)
- **Dark**: #0F172A
- **Light**: #F8FAFC

### Typography
- **Headings**: Poppins (700-900 weight)
- **Body**: Inter (400-600 weight)

### Spacing
- Base unit: 0.5rem (8px)
- Generous padding: 1.4-2rem
- Gap between elements: 0.5-1.3rem

## 🔧 Admin Panel

Access the Django admin at `/admin/` with your superuser credentials to:
- Manage products and categories
- Create blog posts and recipes
- View customer inquiries
- Manage testimonials and USPs
- Configure site settings

## 📱 Responsive Breakpoints

- **Mobile**: < 768px
- **Tablet**: 768px - 991px
- **Desktop**: > 992px

## 🔐 Security Features

- CSRF protection
- SQL injection prevention
- XSS protection
- Secure password hashing
- Environment variable configuration
- .gitignore for sensitive files

## 📝 Environment Variables

```env
DEBUG=False                          # Set to False in production
SECRET_KEY=your-secret-key          # Generate a strong secret key
ALLOWED_HOSTS=yourdomain.com        # Your domain
DATABASE_URL=postgresql://...       # Database connection string
EMAIL_BACKEND=...                   # Email configuration
```

## 🚢 Deployment

### Heroku
```bash
heroku create your-app-name
git push heroku master
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### AWS/DigitalOcean
1. Set up a server with Python and PostgreSQL
2. Clone the repository
3. Configure environment variables
4. Run migrations
5. Collect static files: `python manage.py collectstatic`
6. Use Gunicorn + Nginx for production

## 📊 Database Models

### Products
- Product (name, description, price, category, age_group)
- Category (name, description, icon)
- AgeGroup (name, description, icon)
- ProductImage (product, image)

### Blog
- BlogPost (title, content, author, category, featured_image)
- Recipe (title, ingredients, instructions, difficulty, age_group)
- BlogCategory (name)

### Core
- USP (title, description, icon)
- Testimonial (author, content, rating, avatar)

### Pages
- ContactMessage (name, email, phone, subject, message)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- **Highness Team** - Initial development and design

## 📞 Support

For support, email support@highness.com or open an issue on GitHub.

## 🎯 Roadmap

- [ ] Shopping cart and checkout
- [ ] Payment gateway integration (Razorpay, Stripe)
- [ ] User accounts and order history
- [ ] Wishlist functionality
- [ ] Product reviews and ratings
- [ ] Email notifications
- [ ] SMS alerts
- [ ] Mobile app (React Native)
- [ ] AI-powered product recommendations
- [ ] Subscription boxes

## 📈 Performance

- Optimized images and lazy loading
- Minified CSS and JavaScript
- Database query optimization
- Caching strategies
- CDN-ready static files

## 🔍 SEO

- Meta tags and descriptions
- Structured data (Schema.org)
- Sitemap generation
- Robots.txt configuration
- Mobile-friendly design
- Fast page load times

---

**Made with ❤️ for parents who care about their children's nutrition**
