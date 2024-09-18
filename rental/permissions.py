from rest_framework import permissions


# Clase para permitir solo escritura al autor de un objeto
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):  # Método para comprobar si el usuario es el autor del objeto
        return request.method in permissions.SAFE_METHODS or obj.author == request.user  # Permitir solo lectura a usuarios no autenticados y solo escritura al autor
