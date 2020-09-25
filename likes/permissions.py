from rest_framework.permissions import BasePermission, SAFE_METHODS

from likes.models import Like


class IsOwnerOrReadOnly(BasePermission):
    message = "You must be the owner of this object."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user


class IsOwner(BasePermission):
    message = "You must be owner of this object."

    def has_object_permission(self, request, view, obj):
        return obj.user_id == request.user.id


class NotLikedRecently(BasePermission):
    message = "You have already liked this object!"

    def has_permission(self, request, view):
        return (
            Like.objects.select_related("user", "post")
            .filter(user=request.user, post=request.DATA.get("post", None))
            .exists()
        )
