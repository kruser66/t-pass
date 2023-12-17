from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MusicVenueViewSet, ServiceViewSet, RentalViewSet, UserViewSet

router = DefaultRouter()
router.register(r'musicvenues', MusicVenueViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'rentals', RentalViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
