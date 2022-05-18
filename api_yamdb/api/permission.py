from rest_framework import permissions


class AdminOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.user.is_authenticated and request.user.is_admin
                or request.user.is_superuser is True)

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return (request.user.is_admin
                    or request.user.is_superuser is True)
        return False


class OnlyOwnAccount(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsAdminModeratorOwnerOrReadOnly(permissions.BasePermission):
    """Класс проверяет, что пользователь является автором, админом или
    модератором.
    """

    def has_object_permission(self, request, view, obj):
        if (request.method in permissions.SAFE_METHODS or request.user.is_admin
                or request.user.is_moderator or obj.author == request.user):
            return (request.method in permissions.SAFE_METHODS
                    or request.user.is_admin or request.user.is_moderator
                    or obj.author == request.user)


class AdminOrReadOnly(permissions.BasePermission):
    """Класс проверяет, что пользователь является админом при
    запросах отличных от GET.
    """
    def has_permission(self, request, view):
        if (request.method in permissions.SAFE_METHODS
                or (request.user.is_authenticated and (
                    request.user.is_admin or request.user.is_superuser))):
            return (request.method in permissions.SAFE_METHODS
                    or (request.user.is_authenticated and (
                        request.user.is_admin or request.user.is_superuser)))
