from django.urls import path
from . import views  # Importa las vistas locales

urlpatterns = [
    path('', views.index, name='auth_user'),  # Ruta principal de la app "registro"
]
