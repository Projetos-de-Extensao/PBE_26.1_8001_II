from rest_framework.permissions import BasePermission, SAFE_METHODS

 
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated
 
        return request.user and request.user.is_staff
 
 
class IsAdminUserOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
 
 
# ----- Permissões por perfil (Tarefa: controle de acesso) -----
 
class IsAluno(BasePermission):
    """Permite acesso apenas a usuários autenticados com perfil ALUNO."""
    message = "Apenas alunos podem realizar esta ação."
 
    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.perfil == "ALUNO"
        )
 
 
class IsEmpresa(BasePermission):
    """Permite acesso apenas a usuários autenticados com perfil EMPRESA."""
    message = "Apenas empresas podem realizar esta ação."
 
    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.perfil == "EMPRESA"
        )
 
 
class IsCoordenador(BasePermission):
    """Permite acesso apenas a usuários autenticados com perfil COORDENADOR."""
    message = "Apenas coordenadores podem realizar esta ação."
 
    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.perfil == "COORDENADOR"
        )
 