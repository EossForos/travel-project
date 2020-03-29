from django import forms
from .models import Train
from cities.models import City


class TrainsForm(forms.ModelForm):
    name = forms.CharField(label='Поезд',
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Введите название или номер Поезда'
                               }
                           ))

    departure_city = forms.ModelChoiceField(label='Город отправления', queryset=City.objects.all(),
                                            widget=forms.Select(attrs={'class': 'form-control js-example-basic'}))

    city_of_arrival = forms.ModelChoiceField(label='Город прибытия', queryset=City.objects.all(),
                                             widget=forms.Select(attrs={'class': 'form-control js-example-basic'}))

    travel_time = forms.IntegerField(label='Время в пути',
                                     widget=forms.NumberInput(
                                         attrs={
                                             'class': 'form-control',
                                             'placeholder': 'Время в пути'
                                         }
                                     ))

    class Meta(object):
        model = Train
        fields = ('name', 'departure_city', 'city_of_arrival', 'travel_time')
