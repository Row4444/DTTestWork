from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    get_object_or_404,
)
from rest_framework.permissions import IsAuthenticated

from comments.models import Comment
from comments.permissions import IsOwnerOrReadOnly, IsOwner
from comments.serializers import CommentCreateUpdateSerializer, CommentSerializer


class CommentCreateApiView(CreateAPIView):
    """User create a comment to post"""

    queryset = Comment.objects.all()
    serializer_class = CommentCreateUpdateSerializer
    permissions = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentUpdateAPIView(RetrieveUpdateAPIView):
    """User update comment, if user is owner"""

    serializer_class = CommentCreateUpdateSerializer
    lookup_field = "pk"
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self):
        comment = get_object_or_404(Comment, **self.kwargs)
        self.check_object_permissions(self.request, comment)
        return comment


class CommentDeleteAPIView(DestroyAPIView):
    """User delete comment, if user is owner"""

    serializer_class = CommentSerializer
    lookup_field = "pk"
    permission_classes = [IsOwner]

    def get_object(self):
        comment = get_object_or_404(Comment, **self.kwargs)
        self.check_object_permissions(self.request, comment)
        return comment
