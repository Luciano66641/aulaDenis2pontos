from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro_cliente, name='cadastro_cliente'),
    path('lista/', views.lista_clientes, name='lista_clientes'),
    path('<int:cliente_id>/viagens/', views.cliente_viagens, name='cliente_viagens'),
]
