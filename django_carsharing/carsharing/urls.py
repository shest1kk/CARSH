from django.urls import path
from .views import CityListCreateView, CityDetailView, CarListCreateView, CarDetailView

urlpatterns = [
    path('cities/', CityListCreateView.as_view(), name='city-list-create'),
    path('cities/<int:pk>/', CityDetailView.as_view(), name='city-detail'),
    path('cars/', CarListCreateView.as_view(), name='car-list-create'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
]
