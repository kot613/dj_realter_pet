from django.urls import path
from .views import HousesListView, HouseDetailView, search_house

app_name = 'houses'

urlpatterns = [
    path('list/', HousesListView.as_view(), name='list'),
    path('detail/<int:pk>/', HouseDetailView.as_view(), name='detail'),
    path('search/', search_house, name='search'),
]
