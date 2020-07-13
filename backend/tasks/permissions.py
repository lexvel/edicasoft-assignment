from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow creators of an object to edit it.
    """
    message = 'You must be the owner of this object.'

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
