# schemas.py
from drf_yasg import openapi

# Schema for a single food truck entry
food_truck_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'Applicant': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the Applicant'),
        'Location': openapi.Schema(type=openapi.TYPE_STRING, description='Location coordinates'),
        'Distance': openapi.Schema(type=openapi.TYPE_NUMBER, description='Distance from the given coordinates'),
    },
    example={
        "Applicant": "Off the Grid Services, LLC",
        "Location": "(0.0, 0.0)",
        "Distance": 84.46549662341423
    }
)

# Schema for the API response
example_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'nearest_trucks': openapi.Schema(type=openapi.TYPE_ARRAY, items=food_truck_schema, description='List of nearest food trucks'),
    },
    example={
        "nearest_trucks": [
            {
                "Applicant": "Off the Grid Services, LLC",
                "Location": "(0.0, 0.0)",
                "Distance": 84.46549662341423
            }
        ]
    }
)
