from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
from .models import UserProfile
from .forms import UserProfileForm

class ViewProfile(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'profile.html'

    def get_object(self, queryset=None):
        return self.request.user.userprofile

class EditProfile(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'editprofile.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user.userprofile


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from profiles.models import UserProfile
from .serializers import UserProfileSerializer

@csrf_exempt
@api_view(['GET','POST'])
def lista_perfil(request):
    if request.method == 'GET':
        userProfile = UserProfile.objects.all()
        serializer = UserProfileSerializer(userProfile,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer =  UserProfileSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
