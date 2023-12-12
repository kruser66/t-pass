from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MusicVenueViewSet, ServiceViewSet, RentalViewSet

router = DefaultRouter()
router.register(r'musicvenues', MusicVenueViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'rentals', RentalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
