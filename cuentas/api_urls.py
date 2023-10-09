from django.urls import path
from . import views

urlpatterns = [
    path('api/login/', views.LoginView.as_view(), name='api_login'),
    path('api/register/', views.RegisterView.as_view(), name='api_register'),
    path('api/logout/',  views.logout_view(), name='api_register'),
    path('api/profile/', views.UserProfileView.as_view(), name='api_register'),

]
