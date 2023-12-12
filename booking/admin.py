from django.contrib import admin
from booking.models import MusicVenue, Rental, Service


class InlineService(admin.TabularInline):
    model = Service
    extra = 0


class RentalService(admin.TabularInline):
    model = Rental
    extra = 0


@admin.register(MusicVenue)
class MusicVenueAdmin(admin.ModelAdmin):
    inlines = [
        InlineService,
        RentalService,
    ]


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    pass


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass
