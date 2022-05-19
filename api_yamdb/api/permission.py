from rest_framework import permissions


class AdminOnly(permissions.BasePermission):
    """Класс проверяет, что пользователь является админом."""

    def has_permission(self, request, view):
        return (request.user.is_authenticated and (
                request.user.is_admin
                or request.user.is_superuser))


class OnlyOwnAccount(permissions.BasePermission):
    """Класс проверяет, что пользователь является автором."""

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsAdminModeratorOwnerOrReadOnly(permissions.BasePermission):
    """Класс проверяет, что пользователь является модератором.
    """

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_admin or request.user.is_moderator
                or obj.author == request.user)


class ReadOnly(permissions.BasePermission):
    """Проверка только на чтение."""
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS)


AdminOrReadOnly = ReadOnly | AdminOnly
