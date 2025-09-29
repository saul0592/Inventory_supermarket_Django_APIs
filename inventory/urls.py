from django.urls import path
from . import views

urlpatterns = [
    path('', views.descargar_dataset, name='descargar_dataset'),
]