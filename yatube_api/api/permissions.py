from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    """Класс Разрешений.
    Полный доступ к объекту только у автора."""

    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or request.method in permissions.SAFE_METHODS
        )
