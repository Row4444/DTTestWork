from django.urls import path, include

from posts import views as posts_views
from comments import views as comments_views
from likes import views as likes_views

urlpatterns = [
    path(
        "posts/<int:pk>/delete/",
        posts_views.PostDeleteAPIView.as_view(),
        name="delete_post",
    ),
    path(
        "posts/<int:pk>/update/",
        posts_views.PostUpdateAPIView.as_view(),
        name="update_post",
    ),
    path(
        "posts/<int:pk>/",
        posts_views.PostRetrieveAPIView.as_view(),
        name="retrieve_post",
    ),
    path("posts/create/", posts_views.PostCreateApiView.as_view(), name="create_post"),
    path("posts/", posts_views.PostListAPIView.as_view(), name="list_posts"),
    path(
        "comment/create/",
        comments_views.CommentCreateApiView.as_view(),
        name="create_comment",
    ),
    path(
        "comment/<int:pk>/delete/",
        comments_views.CommentDeleteAPIView.as_view(),
        name="delete_comment",
    ),
    path(
        "comment/<int:pk>/update",
        comments_views.CommentUpdateAPIView.as_view(),
        name="update_comment",
    ),
    path(
        "posts/<int:pk>/like/",
        likes_views.LikeCreateAPIView.as_view(),
        name="create_like",
    ),
    path(
        "posts/<int:pk>/unlike/",
        likes_views.LikeDeleteAPIView.as_view(),
        name="delete_like",
    ),
    path("rest_auth/", include("rest_auth.urls")),
]
