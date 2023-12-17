from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MusicVenue, Service, Rental


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = '__all__'


class MusicVenueSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)
    rentals = RentalSerializer(many=True, read_only=True)

    class Meta:
        model = MusicVenue
        fields = ['id', 'name', 'description', 'address', 'services', 'rentals']


class UserSerializer(serializers.ModelSerializer):
    rentals = RentalSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'rentals']
