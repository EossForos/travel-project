from django.urls import path
from .views import RoutesSearch
from . import views
urlpatterns = [
    path('', RoutesSearch.as_view(), name='routes_search'),
    path('search_results/', views.find_routes, name='search_result'),
]