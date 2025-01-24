# apps/frontal/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # Página principal
]
