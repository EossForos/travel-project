from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import City
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CitiesForm
from django.urls import reverse_lazy



class CityCreate(SuccessMessageMixin, CreateView):
    model = City
    form_class = CitiesForm
    template_name = 'cities/create_city.html'
    success_url = reverse_lazy('cities:cities')
    success_message = 'Город был успешно создан'


class CityUpdate(SuccessMessageMixin, UpdateView):
    model = City
    form_class = CitiesForm
    template_name = 'cities/update_city.html'
    success_url = reverse_lazy('cities:cities')
    success_message = 'Город был успешно обновлён'



class CityDelete(DeleteView):
    model = City
    template_name = 'cities/delete_city.html'
    success_url = reverse_lazy('cities:cities')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Город был успешно удалён')
        return self.post(request, *args, **kwargs)



class CityDetail(DetailView):
    model = City
    context_object_name = 'object'
    success_url = reverse_lazy('cities:cities')
    template_name = 'cities/city_detail.html'



class CityList(ListView):
    model = City
    context_object_name = 'cities'
    paginate_by = 5
    template_name = 'cities/cities.html'


