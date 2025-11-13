from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    User profile model with location information.
    
    TODO: You may need to add additional fields or modify this model.
    Consider adding:
    - Phone number
    - Bio/description
    - Date of birth
    - Profile picture URL
    - Any other relevant fields
    
    The location field is required for the weather API integration task.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    location = models.CharField(max_length=255, blank=True, null=True, help_text="City name for weather lookup")
    phone_number = models.CharField(max_length=10, blank = True, null = True, help_text = 'Enter phone nu')
    date_of_birth = models.DateField(blank = True, null=True)
    bio = models.TextField(blank=True, null=True)
    # TODO: Add more fields as needed
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'user_profiles'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

