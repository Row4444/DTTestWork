from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    message = "You must be the owner of this object."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class IsOwner(BasePermission):
    message = "You must be owner of this object."

    def has_object_permission(self, request, view, obj):
        return obj.author_id == request.user.id
