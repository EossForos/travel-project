from django.core.paginator import Paginator
from django.utils import timezone

from .models import City
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CitiesForm
from django.urls import reverse_lazy



class CityCreate(CreateView):
    model = City
    form_class = CitiesForm
    template_name = 'cities/create_city.html'
    success_url = reverse_lazy('cities')


class CityUpdate(UpdateView):
    model = City
    form_class = CitiesForm
    template_name = 'cities/update_city.html'
    success_url = reverse_lazy('cities')



class CityDelete(DeleteView):
    model = City
    template_name = 'cities/delete_city.html'
    success_url = reverse_lazy('cities')



class CityDetail(DetailView):
    model = City
    context_object_name = 'object'
    template_name = 'cities/city_detail.html'



class CityList(ListView):
    model = City
    template_name = 'cities/cities.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
