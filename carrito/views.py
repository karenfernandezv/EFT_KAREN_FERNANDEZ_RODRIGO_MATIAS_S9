from django.shortcuts import render, redirect
from carrito.shop import Carrito
from carrito.models import Producto
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError



def home(request):
    return render(request, 'home.html')

def crown(request):
    return render(request, 'crown.html')

def lost(request):
    return render(request, 'lost.html')

def pokemonGo(request):
    return render(request, 'pokemonGo.html')

def evolving(request):
    return render(request, 'evolving.html')

def fusion(request):
    return render(request, 'fusion.html')

def shop(request):
    productos = Producto.objects.all()
    return render(request, "astral.html", {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("astral")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("astral")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("astral")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("astral")
