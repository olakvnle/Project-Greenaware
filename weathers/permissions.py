from rest_framework import permissions


class IsAuthenticatedOrReadOnly(permissions):
    """
    Custom permission to allow only authenticated users to access the endpoint.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


class IsAdminUser(permissions.BasePermission):
    """
    Custom permission to allow only admin users to access the endpoint.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
