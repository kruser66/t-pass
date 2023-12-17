from datetime import datetime, timedelta
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
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


class MusicVenueAvailabilityViewSet(viewsets.ViewSet):
    def list(self, request, pk=None):

        music_venue = get_object_or_404(MusicVenue, pk=pk)

        # Берем для тестирования ближайший месяц (30 дней)
        next_month = [datetime.today().date() + timedelta(days=day) for day in range(30)]

        # Получаем список бронирований для площадки на ближайший месяц
        booked_dates = Rental.objects.filter(
            music_venue=music_venue,
            start_date__gte=next_month[0],
            end_date__lte=next_month[-1]
        ).values_list('start_date', 'end_date')

        # Получаем список дат, которые забронированы
        busy_dates = []
        for start, end in booked_dates:
            busy_dates.extend(
                [start + timedelta(days=delta) for delta in range((end - start).days + 1)]
            )

        # Создаем список всех дат, за исключением забронированных
        free_dates = [date for date in next_month if date not in busy_dates]

        return Response(free_dates)


class PastRentalUserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        ]

    def list(self, request):
        # Получаем список всех бронирований текущего пользователя
        rentals = Rental.objects.filter(user=request.user)

        # Фильтруем бронирования по дате
        past_rentals = rentals.filter(end_date__lt=datetime.today())
        future_rentals = rentals.filter(start_date__gt=datetime.today())

        # Создаем сериализаторы для прошедших и будущих бронирований
        past_rental_serializer = RentalSerializer(past_rentals, many=True)
        future_rental_serializer = RentalSerializer(future_rentals, many=True)

        # Создаем ответ с сериализаторами
        data = {
            'past_rentals': past_rental_serializer.data,
            'future_rentals': future_rental_serializer.data,
        }
        return Response(data)
