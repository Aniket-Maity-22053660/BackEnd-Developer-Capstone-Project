from django.shortcuts import render
from rest_framework import generics
from .models import Menu, Booking
from . import serializers
from rest_framework import viewsets
from rest_framework.decorators import permission_classes, throttle_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Menu.objects.all()
    serializer_class = serializers.MenuSerializer
class SingleMenuView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Menu.objects.all()
    serializer_class = serializers.MenuSerializer
class BookingViewSet(viewsets.ModelViewSet):
    #permission_classes = [AllowAny]
    #throttle_classes = [AnonRateThrottle]
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAuthenticated]
    queryset= Booking.objects.all()
    serializer_class= serializers.BookingSerializer
