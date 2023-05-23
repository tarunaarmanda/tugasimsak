from .models import jadwal
from rest_framework import serializers

class jadwalserializer(serializers.ModelSerializer):
    class Meta:
        model = jadwal
        fields = ['id','tanggal','imsak','subuh','terbit','duha','zuhur','asar','magrib','isya']