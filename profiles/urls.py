from django.urls import path, include
from .views import ViewProfile, EditProfile, lista_perfil


urlpatterns = [
    path('profile', ViewProfile.as_view(), name='profile'),
    path('EditProfile', EditProfile.as_view(), name='EditProfile'),
    path('lista_perfil', lista_perfil, name='producto'),
] 