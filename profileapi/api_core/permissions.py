from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow a user to update profile"""

    def has_object_permission(self, request, view, obj):
        """check if user has permission to update profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id


class UpdateOwnFeed(permissions.BasePermission):
    """Allow a user to update feed"""

    def has_object_permission(self, request, view, obj):
        """check if user has permission to update profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id