from rest_framework import generics, permissions
from hearth_api.permissions import IsOwnerOrReadOnly
from .models import Following
from .serializers import FollowingSerializer


class FollowingList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowingSerializer
    queryset = Following.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowingDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FollowingSerializer
    queryset = Following.objects.all()
