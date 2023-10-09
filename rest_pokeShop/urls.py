from django.urls import path, include
from .views import lista_producto


urlpatterns = [
    path('producto', lista_producto, name='producto'),
] 