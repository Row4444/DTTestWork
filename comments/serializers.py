from rest_framework import serializers

from comments.models import Comment


class CommentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("body", "post", "author")


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("author", "body", "date")
