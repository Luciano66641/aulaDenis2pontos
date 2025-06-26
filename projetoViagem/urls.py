from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include(('clientes.urls', 'clientes'), namespace='clientes')),
    path('viagens/', include(('viagens.urls', 'viagens'), namespace='viagens')),
]
