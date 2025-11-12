from rest_framework import serializers
from django.contrib.auth.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    
    TODO: Complete this serializer to handle user registration.
    Requirements:
    - Validate password (minimum 8 characters)
    - Ensure password and password confirmation match
    - Create user with hashed password
    """
    password = serializers.CharField(write_only=True, required=True)
    password_confirm = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password_confirm')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        }
    
    def validate(self, attrs):
        # TODO: Add validation logic here
        # - Check password length (minimum 8 characters)
        # - Check password and password_confirm match
        return attrs
    
    def create(self, validated_data):
        # TODO: Create user with hashed password
        # Remove password_confirm from validated_data before creating user
        pass

