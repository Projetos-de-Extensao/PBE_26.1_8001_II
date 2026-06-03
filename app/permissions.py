from rest_framework.permissions import BasePermission, SAFE_METHODS

from .models import Usuario

 
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated
 
        return request.user and request.user.is_staff
 
 
class IsAdminUserOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class IsAluno(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        user_email = getattr(request.user, "email", None) or getattr(request.user, "username", None)
        if not user_email:
            return False

        return Usuario.objects.filter(email=user_email, perfil="aluno").exists()


class IsEmpresa(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        user_email = getattr(request.user, "email", None) or getattr(request.user, "username", None)
        if not user_email:
            return False

        return Usuario.objects.filter(email=user_email, perfil="empresa").exists()


class IsEmpresaUserOnly(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        user_email = getattr(request.user, "email", None) or getattr(request.user, "username", None)
        if not user_email:
            return False

        return Usuario.objects.filter(email=user_email, perfil="empresa").exists()