# myapp/models.py
from django.db import models

class Car(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    title_status = models.CharField(max_length=100)
    mileage = models.FloatField()
    color = models.CharField(max_length=50)
    vin = models.CharField(max_length=17)
    lot = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
