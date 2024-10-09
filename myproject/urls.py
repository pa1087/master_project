# myapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import CarViewSet  # Adjust this import to match your view class

router = DefaultRouter()
router.register(r'cars', CarViewSet)  # Register the CarViewSet

urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
]

