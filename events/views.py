from django.http import Http404
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer
from hearth_api.permissions import IsOwnerOrReadOnly


class EventList(APIView):
    """
    List all events
    """
    serializer_class = PartySerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(
            events, many=True, context={'request': request}
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
    List individual events
    """
    serializer_class = EventSerializer
    permission_classes = [
        permissions.IsAuthenticated,
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
        serializer = PartySerializer(
            event, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    