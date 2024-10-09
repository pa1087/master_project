from rest_framework import viewsets
from rest_framework.response import Response
from myapp.models import Car  # Change Subject to Car
from myapp.serializers import CarSerializer  # Change SubjectSerializer to CarSerializer

class CarViewSet(viewsets.ModelViewSet):  # Change SubjectViewSet to CarViewSet
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def list(self, request, *args, **kwargs):
        cars = self.get_queryset()
        list_of_strings = [f"{car.brand} {car.model} ({car.year})" for car in cars]  # Adjust to display car details
        return Response(list_of_strings)
