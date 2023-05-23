from django.contrib import admin
from django.urls import path, include

from api.views import JadwalViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('jadwal', JadwalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]