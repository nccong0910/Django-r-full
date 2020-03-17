from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *

# Create your views here.
class UserAPI(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()[:5]

class InfoAPI(viewsets.ModelViewSet):
    serializer_class = InfoSerializer
    queryset = Info.objects.all()[:5]