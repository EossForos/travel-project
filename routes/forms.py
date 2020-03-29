from django import forms
from cities.models import City
from .models import Route

class RouteForm(forms.ModelForm):

    departure_city = forms.ModelChoiceField(label='Город отправления', queryset=City.objects.all(), widget=forms.Select(attrs={'class': 'form-control js-example-basic-single'}))

    city_of_arrival = forms.ModelChoiceField(label='Город прибытия', queryset=City.objects.all(), widget=forms.Select(attrs={'class': 'form-control js-example-basic-single'}))

    across_cities = forms.ModelMultipleChoiceField(label='Через города', queryset=City.objects.all(), required=False, widget=forms.SelectMultiple(attrs={'class': 'form-control js-example-basic-multiple'}))

    travel_time = forms.IntegerField(label='Время в пути',
                                     widget=forms.NumberInput(
                                         attrs={
                                             'class': 'form-control',
                                             'placeholder': 'Время в пути'
                                         }
                                     ))

    class Meta:
        model = Route
        fields = ('departure_city', 'city_of_arrival', 'across_cities', 'travel_time')

