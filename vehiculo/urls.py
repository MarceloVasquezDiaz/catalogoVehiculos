from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.add, name='add'),
    path('guardado/', views.guardado, name='guardado'),
    path('listar/', views.listar, name='listar'),
    # Usuarios
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),
]
