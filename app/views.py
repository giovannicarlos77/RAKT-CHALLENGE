import json
from django.http import JsonResponse
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from scipy.spatial.distance import cdist
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .schemas import example_schema
import numpy as np
import pandas as pd
import math


# Haversine formula to calculate distance between two lat/long points
def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Radius of the Earth in kilometers

    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


# Function to find nearest food trucks using Haversine formula
def find_nearest_food_trucks(latitude, longitude, data, num_results=5):
    # Extract latitude and longitude from the data
    data['Latitude'] = data['Location'].apply(lambda x: float(x.split('(')[1].split(',')[0]))
    data['Longitude'] = data['Location'].apply(lambda x: float(x.split(',')[1].split(')')[0]))

    # Calculate the distance between user location and each food truck using Haversine formula
    data['Distance'] = data.apply(lambda row: haversine(latitude, longitude, row['Latitude'], row['Longitude']), axis=1)

    # Sort the DataFrame by distance and return the top results
    nearest_food_trucks = data.sort_values(by='Distance').head(num_results)
    return nearest_food_trucks[['Applicant', 'Location', 'Distance']]

@method_decorator(csrf_exempt, name='dispatch')
class GetFoodTrucks(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'latitude': openapi.Schema(type=openapi.TYPE_NUMBER, description='Latitude'),
                'longitude': openapi.Schema(type=openapi.TYPE_NUMBER, description='Longitude'),
            }
        ),
        responses={200: openapi.Response('Success', example_schema)}
    )
    def post(self, request):
        try:
            # Parse JSON data from request body
            data = json.loads(request.body)
            latitude = data.get('latitude')
            longitude = data.get('longitude')

            if not latitude or not longitude:
                return JsonResponse({'error': 'Latitude and longitude are required'}, status=400)

            # Find nearest food trucks
            food_trucks_df = pd.read_csv('./food-truck-data.csv')  # Adjust path as necessary
            nearest_trucks = find_nearest_food_trucks(latitude, longitude, food_trucks_df)

            # Convert the result to a list of dictionaries for JSON response
            result = nearest_trucks.to_dict(orient='records')

        except (ValueError, json.JSONDecodeError) as e:
            # Handle parsing errors
            return JsonResponse({'error': 'Invalid input', 'message': str(e)}, status=400)

        return JsonResponse({'nearest_trucks': result}, safe=False)
