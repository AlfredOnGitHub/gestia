from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Página principal de la app de autenticación
    path('', views.auth_user_home, name='auth_user_home'),  # Página principal del módulo auth_user

    # Rutas de autenticación
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

# Rutas para restablecimiento de contraseña
urlpatterns += [
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
