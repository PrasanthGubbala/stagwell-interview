"""
Weather API Service

TODO: Implement integration with WeatherAPI.com

Requirements:
1. Create a function to fetch current weather for a location
2. Handle API errors gracefully (network errors, invalid API key, etc.)
3. Return structured data or raise appropriate exceptions

API Documentation: https://www.weatherapi.com/docs/
API Endpoint: http://api.weatherapi.com/v1/current.json
API Key: Available in Django settings (WEATHER_API_KEY)

Example usage:
    from weather_service import get_weather_for_location
    
    weather_data = get_weather_for_location("London")
    print(weather_data['current']['temp_c'])

Expected response structure:
{
    "location": {
        "name": "London",
        "region": "City of London, Greater London",
        "country": "United Kingdom",
        ...
    },
    "current": {
        "temp_c": 11.0,
        "temp_f": 51.8,
        "condition": {
            "text": "Partly cloudy",
            ...
        },
        ...
    }
}
"""
import requests
from django.conf import settings


def get_weather_for_location(location: str) -> dict:
    """
    Fetch current weather for a given location.
    
    Args:
        location: City name or location string
        
    Returns:
        dict: Weather data from WeatherAPI
        
    Raises:
        requests.RequestException: For network errors
        ValueError: For invalid API responses
    """
    # TODO: Implement this function
    # 1. Get API key from settings.WEATHER_API_KEY
    # 2. Make GET request to http://api.weatherapi.com/v1/current.json
    # 3. Pass location as 'q' parameter and API key as 'key' parameter
    # 4. Handle errors (check response status, handle exceptions)
    # 5. Return JSON response data
    
    api_key = getattr(settings, 'WEATHER_API_KEY', None)
    if not api_key:
        raise ValueError("Weather API key not configured")
    
    # TODO: Implement API call here
    raise NotImplementedError("Weather service not implemented yet")

