from rest_framework import serializers
from .models import MusicVenue, Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class MusicVenueSerializer(serializers.ModelSerializer):

    class Meta:
        model = MusicVenue
        fields = '__all__'
