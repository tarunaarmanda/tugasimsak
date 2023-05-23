from django.shortcuts import render

from .models import jadwal
from .serializers import jadwalserializer
from rest_framework import viewsets, permissions

# Create your views here.

class JadwalViewSet(viewsets.ModelViewSet):
    queryset = jadwal.objects.all()
    serializer_class = jadwalserializer
