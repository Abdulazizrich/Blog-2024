from rest_framework import serializers
from .models import Profil

class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = ['username', 'password', 't_sana', 'davlat']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Profil.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            t_sana=validated_data.get('t_sana', None),
            davlat=validated_data.get('davlat', None)
        )
        return user