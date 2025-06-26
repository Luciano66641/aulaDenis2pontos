from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_viagens, name='lista_viagens'),
    path('nova/', views.nova_viagem, name='nova_viagem'),
    path('<int:viagem_id>/clientes/', views.viagem_por_clientes, name='viagem_por_clientes'),
]
