from django.db import models
from django.contrib.auth.models import User


class MusicVenue(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Музыкальная площадка'
        verbose_name_plural = 'Музыкальные площадки'

    def __str__(self):
        return f'{self.name} - {self.address}'


# предполагаем что каждая площадка свои уникальные услуги представляет
# если какое-то оборудование используется на разных площадках используйте models.ManyToManyFileds
class Service(models.Model):
    music_venue = models.ForeignKey(MusicVenue, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name


# предполагаем, что аренда в целых днях, для почасовой используйте models.DateTimeField
class Rental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rentals')
    music_venue = models.ForeignKey(MusicVenue, on_delete=models.CASCADE, related_name='rentals')
    start_date = models.DateField('Дата начала аренды')
    end_date = models.DateField('Дата окончания аренды')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name
