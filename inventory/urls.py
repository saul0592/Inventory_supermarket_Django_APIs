from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='log_in/log_in.html'), name='login'),
    path('data/', views.descargar_dataset, name='descargar_dataset'),
    
]