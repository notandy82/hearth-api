from rest_framework import generics, permissions
from .models import Party
from .serializers import PartySerializer
from hearth_api.permissions import IsOwnerOrReadOnly


class PartyList(generics.ListCreateAPIView):
    """
    List parties or create a new party if logged in
    """
    serializer_class = PartySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Party.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PartyDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a party, or update or delete it if owner
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PartySerializer
    queryset = Party.objects.all()
