from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Party
from following.models import Following
from profiles.models import Profile
from .serializers import PartySerializer
from hearth_api.permissions import IsOwnerOrReadOnly


class PartyList(generics.ListCreateAPIView):
    """
    List parties or create a new party if logged in
    """
    serializer_class = PartySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Party.objects.annotate(
        posts_count=Count('post', distinct=True),
        followers_count=Count('followed__owner', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend
    ]
    filterset_fields = [
        'followed__owner__profile'
    ]
    ordering_fields = [
        'posts_count'
    ]
    search_fields = [
        'owner__username',
        'title',
        'description',
        'location'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PartyDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a party, or update or delete it if owner
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PartySerializer
    queryset = Party.objects.annotate(
        posts_count=Count('post', distinct=True),
    ).order_by('-created_at')
