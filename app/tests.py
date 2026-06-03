from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate

from .models import Usuario

User = get_user_model()
from .permissions import IsEmpresaUserOnly
from .serializers import UsuarioSerializer


class IsEmpresaUserOnlyPermissionTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.django_user_empresa = User.objects.create_user(
            username="empresa1",
            email="empresa1@example.com",
            password="pass12345",
            nome="Empresa 1",
            perfil="empresa"
        )
        self.django_user_aluno = User.objects.create_user(
            username="aluno1",
            email="aluno1@example.com",
            password="pass12345",
            nome="Aluno 1",
            perfil="aluno"
        )

    def test_empresa_user_is_allowed(self):
        request = self.factory.get("/api/candidaturas/1/aceitar/")
        request.user = self.django_user_empresa

        permission = IsEmpresaUserOnly()
        self.assertTrue(permission.has_permission(request, None))

    def test_non_empresa_user_is_denied(self):
        request = self.factory.get("/api/candidaturas/1/aceitar/")
        request.user = self.django_user_aluno

        permission = IsEmpresaUserOnly()
        self.assertFalse(permission.has_permission(request, None))


class UsuarioSerializerPasswordTest(TestCase):
    def test_password_is_hashed_on_create(self):
        serializer = UsuarioSerializer(data={
            "nome": "User",
            "email": "user@example.com",
            "perfil": "aluno",
            "senha": "senha_segura123"
        })
        self.assertTrue(serializer.is_valid(), serializer.errors)
        usuario = serializer.save()

        self.assertNotEqual(usuario.senha, "senha_segura123")
        self.assertTrue(usuario.check_password("senha_segura123"))
        self.assertFalse(usuario.check_password("senha_errada"))
