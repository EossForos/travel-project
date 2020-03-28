from django.db import models
from django.core.exceptions import ValidationError
from cities.models import City

class Train(models.Model):
    """ Поезд """
    name = models.CharField(max_length=100, unique=True, verbose_name='Имя Поезда')
    departure_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город отправления', related_name='departure_city')
    city_of_arrival = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город прибытия', related_name='city_of_arrival')
    travel_time = models.IntegerField(verbose_name='Время в пути')

    class Meta:
        verbose_name = 'Поезд'
        verbose_name_plural = 'Поезда'
        ordering = ['name']

    def __str__(self):
        return 'Поезд №{} из {} в {}'.format(self.name, self.departure_city, self.city_of_arrival)

    def clean(self, *args, **kwargs):
        if self.departure_city == self.city_of_arrival:
            raise ValidationError('Измените город прибытия ')
        qs = Train.objects.filter(departure_city=self.departure_city, city_of_arrival=self.city_of_arrival, travel_time=self.travel_time).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError('Измените время пути')
        return super(Train, self).clean()
