from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User
from .models import MusicVenue, Service, Rental
from .serializers import MusicVenueSerializer, ServiceSerializer, RentalSerializer, UserSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer


class MusicVenueViewSet(viewsets.ModelViewSet):
    queryset = MusicVenue.objects.all()
    serializer_class = MusicVenueSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
