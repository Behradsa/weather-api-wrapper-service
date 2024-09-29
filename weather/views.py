from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
import requests


class weather_view(APIView):
    def get(self, request):
        location = request.query_params.get("location")
        if location:
            weather_data = self.get_weather_data(location)
        else:
            weather_data = self.get_weather_data()
        return Response(weather_data)

    def get_weather_data(self, location: str = "Tehran"):
        api_key = "GL563UTCNVNT7WLHE8NMHB9NC"
        api_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/"
        if cache.get(location):
            return cache.get(location)
        data = requests.get(api_url, params={"key": api_key}).json()
        cache.set(location, data, timeout=1 * 60)
        return data
