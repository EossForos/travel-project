from django.urls import path
from .views import RoutesSearch, SearchResult

urlpatterns = [
    path('', RoutesSearch.as_view(), name='routes_search'),
    path('search_results/', SearchResult.as_view(), name='search_results'),
]