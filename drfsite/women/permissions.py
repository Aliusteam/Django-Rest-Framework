from rest_framework import permissions


# Определяем доступ для в зависимости от запроса
# Для чтения (безопасный запрос) - для всех
# Для изменения, удаления - только для админа
class IsAdminOrReadOnly(permissions.BasePermission):
    # Изменим ограничение на урове всего запроса
    def has_permission(self, request, view):
        # Если method, который пришел - безопасный
        # то есть: SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
        if request.method in permissions.SAFE_METHODS:
            # True - То права для всех
            return True
        # Иначе, даем достум только для Админа
        return bool(request.user and request.user.is_staff)


# Для изменения статьи - только для Автора этой статьи
class IsOwnerOrReadOnly(permissions.BasePermission):
    # Сдесь разрешение на уровне одной записи - обьекта
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Если пользователь из базы данных равен пользователю, который сделал запрос
        return obj.user == request.user










