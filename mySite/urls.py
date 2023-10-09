"""
URL configuration for mySite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django import views
from django.contrib import admin
from django.urls import path, include
from carrito.views import fusion, evolving, lost, crown, pokemonGo ,home, shop, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito
from django.conf import settings
from django.conf.urls.static import static
from cuentas.views import register_view, login_view,logout_view,UserProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    
    path('crown/', crown, name='crown'),
    path('lost/', lost, name='lost'),
    path('evolving/', evolving, name='evolving'),
    path('fusion/', fusion, name='fusion'),
    path('pokemonGo/', pokemonGo, name='pokemonGo'),
    
    path('registrousuario/', register_view, name='registro'),
    path('cerrarsesion/', logout_view, name='logout'),
    path('iniciosesion/', login_view, name='iniciosesion'),
    path('perfil/', UserProfileView.as_view(), name='profile'),
 
    path('api/', include("rest_pokeShop.urls")),
    path('api/', include('cuentas.urls')),
    path('', include('cuentas.urls')),
  
   
    path('astral/', shop, name="astral"),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


