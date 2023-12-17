from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from .views import (
    MusicVenueViewSet, ServiceViewSet, RentalViewSet,
    PastRentalUserViewSet, MusicVenueAvailabilityViewSet
)

router = DefaultRouter()
router.register(r'musicvenues', MusicVenueViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'rentals', RentalViewSet)
router.register(r'user-rentals', PastRentalUserViewSet, basename='user-rentals')
router.register(
    r'musicvenues/(?P<pk>[^/.]+)/availability',
    MusicVenueAvailabilityViewSet,
    basename='availability'
)

urlpatterns = [
    path('', include(router.urls)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
