from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework import status, filters


class MyCustomPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 100


class MaqolalarAPIView(APIView):


    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="search",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Sarlavha boyicha saralash"
            ),
            openapi.Parameter(
                name="profil",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Profil boyicha qidirish(ID)"
            )

        ]
    )
    def get(self, request):
        maqolalar = Maqola.objects.filter(profil=request.user)
        search = request.query_params.get('search')
        if search is not None:
            maqolalar = maqolalar.filter(sarlavha__contains=search) | maqolalar.filter(batafsil__icontains=search)
        profil = request.query_params.get('profil')
        if profil is not None:
            maqolalar = maqolalar.filter(profil__id=int(profil))
        serializer = MaqolaSerializer(maqolalar, many=True)
        return Response(serializer.data)


class MaqolaCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        request_body=MaqolaPostSerializer,
    )
    def post(self, request):
        serializer = MaqolaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(profil=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MaqolaAPIView(APIView):
    pagination_class = MyCustomPagination

    def get(self, request, pk):
        maqola = get_object_or_404(Maqola, id=pk)
        maqola.korish += 1
        maqola.save()
        serializer = MaqolaSerializer(maqola)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=MaqolaPostSerializer
    )
    def put(self, request, pk):
        maqola = get_object_or_404(Maqola, id=pk)
        if maqola.profil != request.user:
            return Response({"error": "Siz faqat o'zingizga tegishli maqolani tahrirlashingiz mumkin"})
        serializer = MaqolaSerializer(maqola, data=request.data)
        if serializer.is_valid():
            serializer.save(profil=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MaqolalarimAPIView(APIView):
    def get(self, request):
        maqolalar = Maqola.objects.filter(profil=request.user)
        serializer = MaqolaSerializer(maqolalar, many=True)
        return Response(serializer.data)