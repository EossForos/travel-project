from django.contrib import messages
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views import View
from .forms import *

class RoutesSearch(FormView):
    template_name = 'routes/routes_search.html'
    form_class = RouteForm
    success_url = 'routes_search'


class SearchResult(View):
    def find_routes(self, request):
        if request.method == 'POST':
            form = RouteForm(request.POST or None)
            if form.is_valid():
                data = form.changed_data
            return render(request, 'routes/routes_search.html', {'form': form})
        else:
            messages.error(request, 'Создайте маршрут')
            form = RouteForm()
            return render(request, 'routes/routes_search.html', {'form': form})


