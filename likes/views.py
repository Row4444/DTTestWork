from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from likes.models import Like
from likes.permissions import IsOwner, NotLikedRecently
from likes.serializers import LikeSerializer
from posts.models import Post


class LikeCreateAPIView(CreateAPIView):
    """User likes post if like doesn't exists"""

    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permissions = [IsAuthenticated, NotLikedRecently]

    def perform_create(self, serializer):
        post = get_object_or_404(Post, **self.kwargs)
        like = Like.objects.filter(user=self.request.user, post=post)
        if not like.exists():
            serializer.save(user=self.request.user)


class LikeDeleteAPIView(DestroyAPIView):
    """User unlikes post if like exists"""

    serializer_class = LikeSerializer
    permission_classes = [IsOwner]

    def get_object(self):
        post = get_object_or_404(Post, **self.kwargs)
        like = get_object_or_404(Like, post=post, user=self.request.user)
        self.check_object_permissions(self.request, like)
        return like
