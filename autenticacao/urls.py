from django.urls import path, include

from autenticacao import views

urlpatterns = [
    path('login', views.logar, name='login'),
    path('registro', views.registro, name='registro'),
    path('sair', views.sair, name='sair')
]