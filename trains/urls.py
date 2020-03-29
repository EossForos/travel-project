from django.urls import path
from .views import TrainList, TrainCreate, TrainDelete, TrainDetail, TrainUpdate

app_name = 'trains'

urlpatterns = [
    path('', TrainList.as_view(), name='trains'),
    path('create/', TrainCreate.as_view(), name='create'),
    path('detail/<int:pk>/', TrainDetail.as_view(), name='detail'),
    path('update/<int:pk>/', TrainUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', TrainDelete.as_view(), name='delete'),
]