from django.shortcuts import render, get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from rest_framework import generics, permissions, authentication

from .permissions import IsOwnerOrReadOnly, IsOwner
from .serializers import (
    PostListSerializer,
    PostRetrieveSerializer,
    PostCreateUpdateSerializer,
)


class PostListAPIView(generics.ListAPIView):
    """All Posts"""

    permission_classes = (permissions.AllowAny,)
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostRetrieveAPIView(generics.RetrieveAPIView):
    """Detail Post bi id"""

    permission_classes = (permissions.AllowAny,)
    serializer_class = PostRetrieveSerializer
    lookup_field = "id"

    def get_object(self):
        return get_object_or_404(Post, **self.kwargs)


# class PostList(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'posts_list.html'
#
#     def get(self, request):
#         queryset = Post.objects.all()
#         return Response({'posts': queryset})
#
#
# class PostDetail(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'post_detail.html'
#
#     def get(self, request, pk):
#         post = get_object_or_404(Post, pk=pk)
#         return Response({'post': post})


class PostCreateApiView(CreateAPIView):
    """User create Post if User authenticated"""

    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permissions = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostUpdateAPIView(RetrieveUpdateAPIView):
    """User update Post if User is owner"""

    serializer_class = PostCreateUpdateSerializer
    lookup_field = "pk"
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self):
        post = get_object_or_404(Post, **self.kwargs)
        self.check_object_permissions(self.request, post)
        return post

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class PostDeleteAPIView(DestroyAPIView):
    """User delete Post if User is owner"""

    serializer_class = PostRetrieveSerializer
    lookup_field = "pk"
    permission_classes = [IsOwner]

    def get_object(self):
        post = get_object_or_404(Post, **self.kwargs)
        self.check_object_permissions(self.request, post)
        return post
