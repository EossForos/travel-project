from django.contrib import messages
from django.shortcuts import render
from trains.models import Train
from django.views.generic.edit import FormView
from .forms import *

class RoutesSearch(FormView):
    template_name = 'routes/routes_search.html'
    form_class = RouteForm
    success_url = 'routes_search'



def dfs_paths(graph, start, goal):
    """Функция поиска всех возможных маршрутов
       из одного города в другой. Вариант посещения
       одного и того же города более одного раза,
        не рассматривается.
    """
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next_ in graph[vertex] - set(path):
                if next_ == goal:
                    yield path + [next_]
                else:
                    stack.append((next_, path + [next_]))


def get_graph():
    qs = Train.objects.values('city_of_arrival')
    city_of_arrival_set = set(i['city_of_arrival'] for i in qs)
    graph = {}
    for city in city_of_arrival_set:
        trains = Train.objects.filter(city_of_arrival=city).values('departure_city')
        tmp = set(i['departure_city'] for i in trains)
        graph[city] = tmp

    return graph



def find_routes(request):
    if request.method == 'POST':
        form = RouteForm(request.POST or None)
        if form.is_valid():
            data = form.cleaned_data
            city_of_arrival = data['city_of_arrival']
            departure_city = data['departure_city']
            across_cities_form = data['across_cities']
            travel_time = data['travel_time']
            graph = get_graph()
            all_ways = list(dfs_paths(graph, city_of_arrival.id, departure_city.id))
            if len(all_ways) == 0:
                messages.error(request, 'Маршрута, по вашим условиям не существует. ')
                return render(request, 'routes/routes_search.html', {'form': form})
            if across_cities_form:
                across_cities = [city.id for city in across_cities_form]
                right_ways = []
                for way in all_ways:
                    if all(point in way for point in across_cities):
                        right_ways.append(way)
                if not right_ways:
                    messages.error(request, 'Маршрут через эти города не возможен.')
                    return render(request, 'routes/routes_search.html', {'form': form})
                else:
                    right_ways = all_ways
                trains = []
                for route in right_ways:
                    tmp = {}
                    tmp['trains'] = []
                    total_time = 0
                    for index in range(len(route)-1):
                        qs = Train.objects.filter(city_of_arrival=route[index], departure_city=route[index+1])
                        qs = qs.order_by('travel_time').first()
                        total_time += qs.travel_time
                        tmp['trains'].append(qs)
                    tmp['total_time'] = total_time
                    if total_time <= travel_time:
                        trains.append(tmp)
                if not trains:
                    messages.error(request, 'Время в пути больше заданного.')
                    return render(request, 'routes/routes_search.html', {'form': form})
                routes = []
                cities = {'city_of_arrival': city_of_arrival.name, 'departure_city': departure_city.name}
                for tr in trains:
                    routes.append({'route': tr['trains'],
                                   'total_time': tr['total_time'],
                                   'city_of_arrival': city_of_arrival.name,
                                   'departure_city': departure_city.name})
                sorted_routes = []
                if len(routes) == 1:
                    sorted_routes = routes
                else:
                    times = list(set(x['total_time'] for x in routes))
                    times = sorted(times)
                    for time in times:
                        for route in routes:
                            if time == route['total_time']:
                                sorted_routes.append(route)
                context = {}
                form = RouteForm()
                context['form'] = form
                context['routes'] = sorted_routes
                context['cities'] = cities
                return render(request, 'routes/routes_search.html', context)
        return render(request, 'routes/search_result.html', {'form': form})
    else:
        messages.error(request, 'Создайте маршрут')
        form = RouteForm()
        return render(request, 'routes/routes_search.html', {'form': form})


