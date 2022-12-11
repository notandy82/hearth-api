from django.http import Http404
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Party
from .serializers import PartySerializer
from hearth_api.permissions import IsOwnerOrReadOnly


class PartyList(APIView):
    """
    List all parties
    """
    serializer_class = PartySerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        parties = Party.objects.all()
        serializer = PartySerializer(
            parties, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = PartySerializer(
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


class PartyDetail(APIView):
    """
    List individual party
    """
    serializer_class = PartySerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            party = Party.objects.get(pk=pk)
            self.check_object_permissions(self.request, party)
            return party
        except Party.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        party = self.get_object(pk)
        serializer = PartySerializer(
            party, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        party = self.get_object(pk)
        serializer = PartySerializer(
            party, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
