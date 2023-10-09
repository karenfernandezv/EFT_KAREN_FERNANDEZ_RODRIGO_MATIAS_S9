from django.db.models.base import Model
from rest_framework import serializers
from carrito.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'precio','imagen']
        