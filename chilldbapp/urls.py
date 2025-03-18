from django.urls import path
from . import views

urlpatterns = [
    path('', views.db_visualizer, name='db_visualizer'),
]