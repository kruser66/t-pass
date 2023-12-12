from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from booking.views import MusicVenueViewSet, ServiceViewSet, RentalViewSet

router = DefaultRouter()
router.register(r'musicvenues', MusicVenueViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'rentals', RentalViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
