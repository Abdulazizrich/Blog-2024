from rest_framework.serializers import ModelSerializer
from .models import *

class MaqolaSerializer(ModelSerializer):
    class Meta:
        model=Maqola
        fields='__all__'

class MaqolaPostSerializer(ModelSerializer):
    class Meta:
        model=Maqola
        fields=("sarlavha","batafsil")
