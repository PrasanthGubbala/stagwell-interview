# Django Interview Exercise - Setup Guide

This is a Django REST Framework project for a coding interview exercise.

## Prerequisites

- Docker and Docker Compose installed on your system
- That's it! No need to install Python or any dependencies manually.

## Quick Start

1. **Navigate to the project directory:**
   ```bash
   cd coding-interview
   ```

2. **Build and start the containers:**
   ```bash
   docker-compose up --build
   ```
   
   This will:
   - Build the Django application container with all dependencies
   - Start PostgreSQL database
   - Run database migrations automatically
   - Start the Django development server

3. **The API is now available at:**
   ```
   http://localhost:8008/
   ```

## Environment Variables (Optional)

All environment variables are already configured in `docker-compose.yml`, so **you don't need to create a `.env` file** to get started.

If you want to override any settings, you can create a `.env` file with the following variables:

```bash
# Create .env file (optional - only if you need to override defaults)
cat > .env << 'EOF'
SECRET_KEY=django-insecure-change-me-in-production
DEBUG=True
POSTGRES_DB=interview_db
POSTGRES_USER=interview_user
POSTGRES_PASSWORD=interview_pass
POSTGRES_HOST=db
POSTGRES_PORT=5432
WEATHER_API_KEY=8776024c3d6b46e6a35192629251211
EOF
```

**Note:** The `.env` file is completely optional. The project will work without it since all variables are already set in `docker-compose.yml`.

4. **Create a superuser (optional, for Django admin):**
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

## Project Structure

```
coding-interview/
├── authentication/          # Authentication app (JWT)
│   ├── views.py            # Register/Login endpoints
│   ├── serializers.py      # User registration serializer
│   └── urls.py             # Auth URL patterns
├── profiles/               # User profiles app
│   ├── models.py          # UserProfile model
│   ├── views.py           # Profile CRUD endpoints (to be implemented)
│   ├── serializers.py     # Profile serializers (to be implemented)
│   └── urls.py            # Profile URL patterns (to be implemented)
├── tests/                  # Test files
│   ├── test_authentication.py
│   └── test_profiles.py
├── interview_project/      # Django project settings
│   ├── settings.py        # Django configuration
│   └── urls.py            # Root URL configuration
├── weather_service.py      # Weather API integration (to be implemented)
├── conftest.py            # Pytest fixtures
├── pytest.ini             # Pytest configuration
├── requirements.txt       # Python dependencies
├── docker-compose.yml     # PostgreSQL service
├── manage.py              # Django management script
├── INSTRUCTIONS.md        # Exercise instructions
└── README.md             # This file
```

## Running Tests

Run all tests inside the container:
```bash
docker-compose exec web pytest
```

Run tests with coverage report:
```bash
docker-compose exec web pytest --cov=authentication --cov=profiles --cov-report=term-missing
```

Generate HTML coverage report:
```bash
docker-compose exec web pytest --cov=authentication --cov=profiles --cov-report=html
# The htmlcov/ directory will be created in your project folder
# Open htmlcov/index.html in your browser
```

## API Endpoints

### Authentication
- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Login and get JWT tokens

### Profiles (Requires Authentication)
- `GET /api/profiles/` - List all profiles
- `GET /api/profiles/{id}/` - Retrieve specific profile
- `POST /api/profiles/` - Create profile
- `PUT /api/profiles/{id}/` - Update profile
- `PATCH /api/profiles/{id}/` - Partial update profile
- `DELETE /api/profiles/{id}/` - Delete profile

## Managing Containers

**Stop the containers:**
```bash
docker-compose down
```

**Stop and remove volumes (fresh start - use this if you get database errors):**
```bash
docker-compose down -v
docker-compose up --build
```

**Note:** The `-v` flag removes all volumes, including the database. This is useful if you encounter database connection errors or want to start completely fresh.

**View logs:**
```bash
docker-compose logs -f web
```

**Run Django management commands:**
```bash
# Make migrations
docker-compose exec web python manage.py makemigrations

# Run migrations
docker-compose exec web python manage.py migrate

# Access Django shell
docker-compose exec web python manage.py shell
```

**Run commands in the container:**
```bash
docker-compose exec web bash
```

## Troubleshooting

**Issue: Cannot connect to database / "database does not exist" error**
- This usually happens if there's stale data in the PostgreSQL volume
- **Solution:** Reset the database volume:
  ```bash
  docker-compose down -v
  docker-compose up --build
  ```
- Make sure Docker is running
- Check that `docker-compose up` completed successfully
- Wait a few seconds for the database to be ready (healthcheck should pass)

**Issue: Port 8008 already in use**
- Stop any other services using port 8008
- Or modify the port mapping in `docker-compose.yml` (e.g., `"8009:8000"`)

**Issue: Migration errors**
- Try running: `docker-compose exec web python manage.py migrate --run-syncdb`
- If issues persist, reset everything: `docker-compose down -v && docker-compose up --build`

**Issue: Changes not reflecting**
- The project uses volume mounting, so changes should reflect immediately
- If not, restart the web container: `docker-compose restart web`

**Issue: Container build fails**
- Make sure Docker has enough resources allocated
- Try: `docker-compose build --no-cache`

## Next Steps

Read `INSTRUCTIONS.md` for detailed task requirements and guidelines.

Good luck with the exercise!

