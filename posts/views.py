from django.db.models import Count
from .models import Post
from rest_framework import permissions, generics
from .serializers import PostSerializer
from hearth_api.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count=Count('likes', distinct=True),
        likes_count=Count('comments', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    retrieve individual post, edit or delete if logged in
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.annotate(
        comments_count=Count('likes', distinct=True),
        likes_count=Count('comments', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter
    ]
