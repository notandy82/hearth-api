from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import EventSerializer
from .models import Event
from rest_framework.response import Response
from rest_framework import status, permissions
from hearth_api.permissions import IsOwnerOrReadOnly


class EventList(APIView):
    """
    List all events
    """
    serializer_class = EventSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        parties = Event.objects.all()
        serializer = EventSerializer(
            parties, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

class EventDetail(APIView):
    """
    List individual party
    """
    serializer_class = EventSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            event = Event.objects.get(pk=pk)
            self.check_object_permissions(self.request, event)
            return event
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        event = self.get_object(pk)
        serializer = EventSerializer(
            event, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        event = self.get_object(pk)
        serializer = EventSerializer(
            event, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
