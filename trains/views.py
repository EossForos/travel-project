from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from trains.forms import TrainsForm
from .models import Train
from django.views.generic import ListView


class TrainCreate(SuccessMessageMixin, CreateView):
    model = Train
    form_class = TrainsForm
    template_name = 'trains/create_train.html'
    success_url = reverse_lazy('trains')
    success_message = 'Поезд был успешно создан'


class TrainUpdate(SuccessMessageMixin, UpdateView):
    model = Train
    form_class = TrainsForm
    template_name = 'trains/update_train.html'
    success_url = reverse_lazy('trains')
    success_message = 'Поезд был успешно обновлён'



class TrainDelete(DeleteView):
    model = Train
    template_name = 'trains/delete_train.html'
    success_url = reverse_lazy('trains')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Поезд был успешно удалён')
        return self.post(request, *args, **kwargs)



class TrainDetail(DetailView):
    model = Train
    context_object_name = 'object'
    template_name = 'trains/train_detail.html'


class TrainList(ListView):
    model = Train
    context_object_name = 'trains'
    paginate_by = 5
    template_name = 'trains/trains.html'