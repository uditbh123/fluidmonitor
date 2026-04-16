from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_reading, name='add_reading'),
    path('chart-data/', views.chart_data, name='chart_data'),
    path('delete/<int:pk>/', views.delete_reading, name='delete_reading'),
]