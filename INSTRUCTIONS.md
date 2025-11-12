# Coding Interview Exercise - Instructions

## Overview

You have approximately **45 minutes** to complete this exercise. The goal is to build a User Profile Management API using Django and Django REST Framework.

## Setup Instructions

1. **Build and start the containers:**
   ```bash
   docker-compose up --build
   ```
   
   This will automatically:
   - Build the Django application with all dependencies
   - Start PostgreSQL database
   - Run database migrations
   - Start the development server
   
   **Note:** You don't need to create a `.env` file - all environment variables are already configured in `docker-compose.yml`.
   
   The API will be available at `http://localhost:8008/`

2. **Create a superuser** (optional, for admin access):
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

3. **That's it!** You can now start coding. All dependencies are installed in the container.
   
   **Note:** Your code changes will be reflected immediately thanks to volume mounting. If you need to restart the server:
   ```bash
   docker-compose restart web
   ```

## Core Tasks (Must Complete - ~30-35 minutes)

### Task 1: Authentication (~10 minutes)

**Objective:** Implement JWT-based authentication endpoints.

**What to do:**
1. Complete the `UserRegistrationSerializer` in `authentication/serializers.py`:
   - Validate password (minimum 8 characters)
   - Ensure password and password_confirm match
   - Create user with hashed password

2. Complete the `register` view in `authentication/views.py`:
   - Validate user data
   - Create new user
   - Return JWT tokens (access and refresh) upon successful registration

3. Complete the `login` view in `authentication/views.py`:
   - Authenticate user with username and password
   - Return JWT tokens upon successful authentication

4. Write unit tests in `tests/test_authentication.py`:
   - Test registration with valid/invalid data
   - Test login with valid/invalid credentials
   - Test that tokens are returned

**Note:** Run tests inside the container:
```bash
docker-compose exec web pytest tests/test_authentication.py
```

**Endpoints to implement:**
- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Login and get JWT tokens

**Expected Response Format:**
```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "user": {
        "id": 1,
        "username": "testuser",
        "email": "test@example.com"
    }
}
```

### Task 2: Database Operations (~15 minutes)

**Objective:** Implement CRUD operations for user profiles using PostgreSQL.

**What to do:**
1. Review and potentially enhance the `UserProfile` model in `profiles/models.py`
   - The model already has a `location` field (required for Task 4)
   - Consider adding additional fields if needed

2. Create `UserProfileSerializer` in `profiles/serializers.py`:
   - Serialize user profile data
   - Include user information (nested or flat)
   - Add validation for location field

3. Create views in `profiles/views.py`:
   - List profiles (GET `/api/profiles/`)
   - Retrieve profile (GET `/api/profiles/{id}/`)
   - Create profile (POST `/api/profiles/`)
   - Update profile (PUT/PATCH `/api/profiles/{id}/`)
   - Delete profile (DELETE `/api/profiles/{id}/`)

4. Create URL patterns in `profiles/urls.py`

5. Write unit tests in `tests/test_profiles.py`:
   - Test all CRUD operations
   - Test authentication requirements
   - Test that users can only modify their own profile (bonus)

**Note:** Run tests inside the container:
```bash
docker-compose exec web pytest tests/test_profiles.py
```

**Endpoints to implement:**
- `GET /api/profiles/` - List all profiles
- `GET /api/profiles/{id}/` - Retrieve specific profile
- `POST /api/profiles/` - Create profile
- `PUT /api/profiles/{id}/` - Update profile (full update)
- `PATCH /api/profiles/{id}/` - Update profile (partial update)
- `DELETE /api/profiles/{id}/` - Delete profile

**Note:** All profile endpoints should require authentication.

### Task 3: Unit Tests (~10 minutes)

**Objective:** Write comprehensive unit tests and achieve at least 70% code coverage.

**What to do:**
1. Complete tests in `tests/test_authentication.py`
2. Complete tests in `tests/test_profiles.py`
3. Run tests and check coverage:
   ```bash
   docker-compose exec web pytest --cov=authentication --cov=profiles --cov-report=term-missing
   ```

**Coverage Target:** Minimum 70% code coverage

## Advanced Tasks (If Time Permits - ~10-15 minutes)

### Task 4: External API Integration

**Objective:** Integrate with WeatherAPI.com to fetch weather data for user locations.

**What to do:**
1. Complete the `get_weather_for_location` function in `weather_service.py`:
   - Make API calls to WeatherAPI.com
   - Handle errors gracefully (network errors, invalid responses, etc.)
   - Return structured weather data

2. Add a new endpoint in `profiles/views.py`:
   - `GET /api/profiles/{id}/weather/` - Get weather for profile's location
   - This endpoint should:
     - Retrieve the user profile
     - Get the location from the profile
     - Call the weather service
     - Return weather data

3. Write tests for the weather service:
   - Mock the external API calls
   - Test error handling
   - Test successful responses

**Note:** Run tests inside the container:
```bash
docker-compose exec web pytest
```

**API Information:**
- Base URL: `http://api.weatherapi.com/v1/current.json`
- API Key: Already configured in settings (no need to create one)
- Documentation: https://www.weatherapi.com/docs/

**Example API Call:**
```
GET http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=London
```

### Task 5: Bonus Features (Optional)

If you have extra time, consider implementing:
- Add validation to profile model (e.g., phone number format, email validation)
- Add pagination to list endpoints
- Add filtering/search capabilities (e.g., search by location, username)
- Add rate limiting
- Add API documentation (Swagger/OpenAPI)

## Testing Your Implementation

1. **Run the test suite:**
   ```bash
   docker-compose exec web pytest
   ```

2. **Check code coverage:**
   ```bash
   docker-compose exec web pytest --cov=authentication --cov=profiles --cov-report=html
   # The htmlcov/ directory will be created in your project folder
   # Open htmlcov/index.html in your browser
   ```

3. **Test endpoints manually:**
   The server should already be running at `http://localhost:8008/`
   
   ```bash
   # Register a user
   curl -X POST http://localhost:8008/api/auth/register/ \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "email": "test@example.com", "password": "testpass123", "password_confirm": "testpass123"}'
   
   # Login
   curl -X POST http://localhost:8008/api/auth/login/ \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "password": "testpass123"}'
   
   # Create profile (use token from login)
   curl -X POST http://localhost:8008/api/profiles/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -d '{"location": "London"}'
   ```

## Code Quality Guidelines

- Write clean, readable code
- Follow PEP 8 style guidelines
- Add docstrings to functions and classes
- Handle errors appropriately
- Write meaningful test names
- Keep functions focused and small

## Evaluation Criteria

Your code will be evaluated on:
1. **Functionality** - Does it work correctly?
2. **Code Quality** - Is the code clean and well-structured?
3. **Test Coverage** - Are there sufficient unit tests? (Target: 70%+)
4. **Error Handling** - Are errors handled gracefully?
5. **Best Practices** - Are Django/DRF best practices followed?

## Questions?

If you have any questions during the exercise, feel free to ask. Good luck!

