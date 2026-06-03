from rest_framework.permissions import BasePermission, SAFE_METHODS


# ----- Permissões já existentes (não mexer) -----


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated

        return request.user and request.user.is_staff


class IsAdminUserOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


# ----- Permissões por perfil (controle de acesso) -----


class IsAluno(BasePermission):
    """Permite acesso apenas a usuários com perfil 'aluno'."""
    message = "Apenas alunos podem realizar esta ação."

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and getattr(request.user, "perfil", None) == "aluno"
        )


class IsEmpresa(BasePermission):
    """Permite acesso apenas a usuários com perfil 'empresa'."""
    message = "Apenas empresas podem realizar esta ação."

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and getattr(request.user, "perfil", None) == "empresa"
        )


class IsEmpresaUserOnly(BasePermission):
    """Compatibilidade com testes antigos: permite apenas `perfil == 'empresa'`."""

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and getattr(request.user, "perfil", None) == "empresa"
        )


class IsCoordenador(BasePermission):
    """Permite acesso apenas a usuários com perfil 'coordenador'."""
    message = "Apenas coordenadores podem realizar esta ação."

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and getattr(request.user, "perfil", None) == "coordenador"
        )