from django.urls import path
from .views import CityDetail, CityCreate, CityUpdate, CityDelete, CityList

urlpatterns = [
    path('', CityList.as_view(), name='cities'),
    path('create/', CityCreate.as_view(), name='create'),
    path('detail/<int:pk>/', CityDetail.as_view(), name='detail'),
    path('update/<int:pk>/', CityUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', CityDelete.as_view(), name='delete'),
]