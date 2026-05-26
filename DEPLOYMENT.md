# Deployment & GitHub Setup Guide

## 📦 Repository Setup

Your local repository is now initialized with 3 commits:

```
8d88daa Add MIT License
cadefce Add comprehensive README documentation
8ca0ba7 Initial commit: Highness cerelac e-commerce platform with modern design
```

## 🚀 Push to GitHub

### Step 1: Create Repository on GitHub

1. Go to [GitHub](https://github.com/new)
2. Create a new repository named `highness` (or your preferred name)
3. **Do NOT** initialize with README, .gitignore, or license (we already have these)
4. Click "Create repository"

### Step 2: Add Remote and Push

```bash
# Navigate to project directory
cd /home/cis/Desktop/osama-workspace/slurrp_farm_clone

# Add remote repository
git remote add origin https://github.com/YOUR_USERNAME/highness.git

# Rename branch to main (optional but recommended)
git branch -M main

# Push to GitHub
git push -u origin main
```

### Step 3: Verify

Visit `https://github.com/YOUR_USERNAME/highness` to confirm your code is pushed.

## 🔐 GitHub Configuration

### Add Collaborators
1. Go to Settings → Collaborators
2. Add team members by username or email

### Enable Branch Protection
1. Go to Settings → Branches
2. Add rule for `main` branch
3. Require pull request reviews before merging
4. Require status checks to pass

### Set Up GitHub Actions (CI/CD)

Create `.github/workflows/django.yml`:

```yaml
name: Django Tests

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Run migrations
      run: python manage.py migrate
    
    - name: Run tests
      run: python manage.py test
```

## 🐳 Docker Setup (Optional)

Create `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "slurrpfarm.wsgi:application", "--bind", "0.0.0.0:8000"]
```

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
      - SECRET_KEY=your-secret-key
    volumes:
      - .:/app
```

Run with: `docker-compose up`

## 🌐 Deployment Platforms

### Heroku

```bash
# Install Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# Login to Heroku
heroku login

# Create app
heroku create your-app-name

# Add PostgreSQL
heroku addons:create heroku-postgresql:hobby-dev

# Set environment variables
heroku config:set DEBUG=False
heroku config:set SECRET_KEY=your-secret-key

# Push code
git push heroku main

# Run migrations
heroku run python manage.py migrate

# Create superuser
heroku run python manage.py createsuperuser

# View logs
heroku logs --tail
```

### PythonAnywhere

1. Sign up at [PythonAnywhere](https://www.pythonanywhere.com)
2. Create a new web app
3. Clone your GitHub repository
4. Configure virtual environment
5. Set up WSGI file
6. Configure static files

### AWS (EC2 + RDS)

```bash
# SSH into EC2 instance
ssh -i your-key.pem ec2-user@your-instance-ip

# Install dependencies
sudo yum update -y
sudo yum install python3 python3-pip postgresql-devel -y

# Clone repository
git clone https://github.com/YOUR_USERNAME/highness.git
cd highness

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Configure environment
nano .env

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Install Gunicorn
pip install gunicorn

# Run Gunicorn
gunicorn slurrpfarm.wsgi:application --bind 0.0.0.0:8000
```

### DigitalOcean App Platform

1. Connect your GitHub repository
2. Select Python as runtime
3. Set environment variables
4. Deploy

## 📊 Monitoring & Logging

### Sentry (Error Tracking)

```bash
pip install sentry-sdk
```

Add to `settings.py`:

```python
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="your-sentry-dsn",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True
)
```

### CloudWatch (AWS Logging)

```bash
pip install watchtower
```

## 🔄 Continuous Integration

### GitHub Actions Secrets

1. Go to Settings → Secrets
2. Add secrets:
   - `SECRET_KEY`
   - `DATABASE_URL`
   - `DEBUG`

## 📝 Git Workflow

### Feature Branch Workflow

```bash
# Create feature branch
git checkout -b feature/amazing-feature

# Make changes and commit
git add .
git commit -m "Add amazing feature"

# Push to GitHub
git push origin feature/amazing-feature

# Create Pull Request on GitHub
# After review and approval, merge to main
```

### Commit Message Convention

```
<type>(<scope>): <subject>

<body>

<footer>
```

Types: feat, fix, docs, style, refactor, test, chore

Example:
```
feat(products): add product filtering by age group

- Implement age-based product filtering
- Add filter UI component
- Update product list view

Closes #123
```

## 🔐 Security Checklist

- [ ] Change `SECRET_KEY` in production
- [ ] Set `DEBUG=False` in production
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Use HTTPS only
- [ ] Set secure cookies
- [ ] Enable CSRF protection
- [ ] Use environment variables for secrets
- [ ] Regular security updates
- [ ] Database backups
- [ ] Monitor error logs

## 📞 Support

For deployment issues:
1. Check logs: `heroku logs --tail` or `docker logs container-id`
2. Review Django error messages
3. Check environment variables
4. Verify database connection
5. Test locally first

---

**Happy deploying! 🚀**
