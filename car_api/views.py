
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Car
from .serializer import CarSerializer
# Create your views here.

class CarList(ListCreateAPIView):
    queryset= Car.objects.all()
    serializer_class = CarSerializer


class CarDetail(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
 