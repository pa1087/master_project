from django.contrib import admin
from .models import Car  # Change this line to import Car instead of Subject

admin.site.register(Car)  # Register the Car model with the admin site
