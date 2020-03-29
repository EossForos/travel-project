from django.db import models
from trains.models import Train


class Route(models.Model):
    """  Маршрут """
    name = models.CharField(max_length=100, verbose_name='Название маршрута', unique=True)
    departure_city = models.CharField(max_length=100, verbose_name='Город отправления')
    city_of_arrival = models.CharField(max_length=100, verbose_name='Город прибытия')
    across_cities = models.ManyToManyField(Train, blank=True, verbose_name='Через города', )
    travel_time = models.IntegerField(verbose_name='Время в пути')

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
        ordering = ['name']

    def __str__(self):
        return self.name

