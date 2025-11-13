from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """
    User registration endpoint.
    
    TODO: Complete this endpoint to:
    1. Validate user data using UserRegistrationSerializer
    2. Create new user
    3. Return JWT tokens (access and refresh) upon successful registration
    
    Expected request body:
    {
        "username": "testuser",
        "email": "test@example.com",
        "password": "securepassword123",
        "password_confirm": "securepassword123"
    }
    
    Expected response (201):
    {
        "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
        "user": {
            "id": 1,
            "username": "testuser",
            "email": "test@example.com"
        }
    }
    """
    serializer = UserRegistrationSerializer(data=request.data)
    
    # TODO: Add validation and user creation logic here
    # Hint: Use serializer.is_valid(), serializer.save(), and RefreshToken
    if serializer.is_valid():
        user = serializer.save()
        tokens = get_tokens(user) # TODO 
        return Response( {
        "access": tokens['access'],
        "refresh": tokens['refresh'],
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    }, status = status.HTTP_201_CREATED)
    
    return Response(
        {"detail": "Registration endpoint not implemented yet"},
        status=status.HTTP_501_NOT_IMPLEMENTED
    )


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """
    User login endpoint.
    
    TODO: Complete this endpoint to:
    1. Authenticate user with username and password
    2. Return JWT tokens (access and refresh) upon successful authentication
    
    Expected request body:
    {
        "username": "testuser",
        "password": "securepassword123"
    }
    
    Expected response (200):
    {
        "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
        "user": {
            "id": 1,
            "username": "testuser",
            "email": "test@example.com"
        }
    }
    
    Expected response for invalid credentials (401):
    {
        "detail": "Invalid credentials"
    }
    """
    username = request.data.get('username')
    password = request.data.get('password')
    
    # TODO: Add authentication logic here
    # Hint: Use User.objects.get() and user.check_password()
    # Then generate tokens using RefreshToken
    user = User.objects.get(username = username)
    if not user.check_password(password):
        raise Exception('INvalid')
    except User.DoesNotExist:
        return Response({"detail" : 'Invalid credentials'})


    tokens = get_tokens(user)
    return Response( {
        "access":tokens['access'] ,
        "refresh":tokens['refresh'],
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    }, status = status.HTTP_200_OK)



