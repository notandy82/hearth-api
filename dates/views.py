from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import EventSerializer
from .models import Event
from rest_framework.response import Response
from rest_framework import status, permissions


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
