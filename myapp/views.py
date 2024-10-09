# myapp/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from myapp.models import Car  # Ensure this imports your Car model
from myapp.serializers import CarSerializer  # Ensure this serializer is created for your Car model

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()  # Adjust this to reflect the queryset for your Car model
    serializer_class = CarSerializer  # Adjust this to reflect the serializer for your Car model

    def list(self, request, *args, **kwargs):
        cars = self.get_queryset()
        car_list = [f"{car.brand} {car.model} ({car.year})" for car in cars]  # Customize this to display the car's information
        return Response(car_list)

    # Optionally, you can override other methods like create, update, delete if needed.
