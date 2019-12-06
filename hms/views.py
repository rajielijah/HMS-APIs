from django.shortcuts import render
from .serializers import HostelSerializer, BlockSerializer, RoomSerializer, WardenSerializer
from .models import *
from rest_framework import viewsets

class HostelView(viewsets.ModelViewSet):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer

class BlockView(viewsets.ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer

class RoomView(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class WardenView(viewsets.ModelViewSet):
    queryset = Warden.objects.all()
    serializer_class = WardenSerializer