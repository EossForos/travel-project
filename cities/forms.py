from django import forms
from .models import City



class CitiesForm(forms.ModelForm):

    name = forms.CharField(label='Город',
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Введите название города'
                               }
                           ))

    class Meta:
        model = City
        fields = ('name', )