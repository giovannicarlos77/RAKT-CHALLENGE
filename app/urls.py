from django.urls import path
from .views import GetFoodTrucks

urlpatterns = [
    path('get-food-trucks/', GetFoodTrucks.as_view(), name='get-food-trucks-api'),
]