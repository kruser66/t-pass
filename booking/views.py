from rest_framework import viewsets
from .models import MusicVenue, Service, Rental
from .serializers import MusicVenueSerializer, ServiceSerializer, RentalSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer


class MusicVenueViewSet(viewsets.ModelViewSet):
    queryset = MusicVenue.objects.all()
    serializer_class = MusicVenueSerializer
