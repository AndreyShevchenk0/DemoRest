#from django.shortcuts import render
from rest_framework import generics
from cars.serializers import CarDetailSerializer, CarsListSerializer
from cars.models import Car
from cars.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveUpdateDestroyAPIView


# создание
class CarCreateView(generics.CreateAPIView,):
    serializer_class = CarDetailSerializer


class CarsListView(generics.ListAPIView):
    serializer_class = CarsListSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticated,)  # или IsAdminUser***********

# Просмотр конкретних записей, редактирование и удаление!

class CarDetailView( RetrieveUpdateDestroyAPIView):  # метод #generics перед Retrieve закоментил
    serializer_class = CarDetailSerializer                # испитания
    queryset = Car.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
    #name = 'coment_list'
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
