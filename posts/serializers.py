from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import HyperlinkedIdentityField

from comments.serializers import CommentSerializer
from likes.models import Like
from .models import Post


class PostListSerializer(serializers.ModelSerializer):
    url = HyperlinkedIdentityField(view_name="retrieve_post")

    class Meta:
        model = Post
        fields = ("url", "id", "author", "title", "body", "date_of_create")


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "body")


class PostRetrieveSerializer(serializers.ModelSerializer):
    can_like = serializers.SerializerMethodField(read_only=True)
    likes = serializers.comments = SerializerMethodField(read_only=True)
    comment_set = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = (
            "author",
            "title",
            "body",
            "date_of_create",
            "likes",
            "comment_set",
            "can_like",
        )

    def get_likes(self, obj):
        return Like.objects.select_related("post").filter(post=obj).count()

    def get_can_like(self, obj):
        request = self.context.get("request")
        if request.user.is_authenticated:
            liked_recently = Like.objects.select_related("user", "post").filter(
                user=request.user,
                post=obj,
            )
            if not liked_recently.exists():
                return True
        return False
