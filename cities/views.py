from .models import City
from django.shortcuts import render

def cities(request):
    cities = City.objects.all()

    context = {
        'cities': cities,
    }

    return render(request, 'cities/cities.html', context)



