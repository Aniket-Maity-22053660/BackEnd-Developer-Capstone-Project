from django.shortcuts import render
from rest_framework import generics
from .models import Menu, Booking
from . import serializers
from rest_framework import viewsets
# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuView(generics.ListCreateAPIView):
    queryset=Menu.objects.all()
    serializer_class = serializers.MenuSerializer
class SingleMenuView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Menu.objects.all()
    serializer_class = serializers.MenuSerializer
class BookingViewSet(viewsets.ModelViewSet):
    queryset= Booking.objects.all()
    serializer_class= serializers.BookingSerializer
