from rest_framework.permissions import (IsAuthenticated,
                                        SAFE_METHODS)


class AuthorOrReadOnly(IsAuthenticated):
    """Класс Разрешений.
    Полный доступ к объекту только у автора."""

    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or request.method in SAFE_METHODS
        )
