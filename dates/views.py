from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import EventSerializer
from .models import Event
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from hearth_api.permissions import IsOwnerOrReadOnly


class EventList(generics.ListCreateAPIView):
    """
    List all events
    """
    serializer_class = EventSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Event.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete event by ID if owner
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = EventSerializer
    queryset = Event.objects.all()
