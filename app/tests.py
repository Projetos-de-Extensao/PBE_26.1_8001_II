"""
Testes automatizados — Sistema de Gestão de Estágios (IBM8936)
Cobertura: autenticação JWT, candidaturas, filtros, permissões, integração
"""

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory, force_authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from .models import (
    Usuario, Aluno, Empresa, Professor, Coordenador,
    Vaga, Candidatura, Estagio
)
from .permissions import IsAluno, IsEmpresa, IsEmpresaUserOnly, IsAdminOrReadOnly, IsAdminUserOnly


# ─────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────

def make_usuario(nome, email, perfil, password="pass@1234", is_staff=False):
    """Cria um Usuario e retorna a instância."""
    u = Usuario.objects.create_user(
        email=email,
        password=password,
        nome=nome,
        perfil=perfil,
    )
    if is_staff:
        u.is_staff = True
        u.save()
    return u


def jwt_client(usuario):
    """Retorna um APIClient já autenticado via JWT Bearer."""
    client = APIClient()
    refresh = RefreshToken.for_user(usuario)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
    return client


# ─────────────────────────────────────────────
# 1. AUTENTICAÇÃO JWT
# ─────────────────────────────────────────────

class JWTAuthTest(TestCase):
    """Testa geração e uso de tokens JWT."""

    def setUp(self):
        self.client = APIClient()
        self.usuario = make_usuario("Aluno JWT", "jwt@test.com", "aluno")
        self.url_token = "/api/token/"
        self.url_refresh = "/api/token/refresh/"

    def test_obter_token_com_credenciais_validas(self):
        resp = self.client.post(self.url_token, {
            "email": "jwt@test.com",
            "password": "pass@1234"
        })
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertIn("access", resp.data)
        self.assertIn("refresh", resp.data)

    def test_obter_token_com_senha_errada(self):
        resp = self.client.post(self.url_token, {
            "email": "jwt@test.com",
            "password": "senhaerrada"
        })
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_refresh_token_valido(self):
        refresh = RefreshToken.for_user(self.usuario)
        resp = self.client.post(self.url_refresh, {"refresh": str(refresh)})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertIn("access", resp.data)

    def test_acesso_sem_token_retorna_401(self):
        resp = self.client.get("/api/vagas/")
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_acesso_com_token_invalido_retorna_401(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer tokeninvalido")
        resp = self.client.get("/api/vagas/")
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_acesso_com_token_valido_retorna_200(self):
        client = jwt_client(self.usuario)
        resp = client.get("/api/vagas/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)


# ─────────────────────────────────────────────
# 2. PERMISSÕES (unit — sem hit de banco)
# ─────────────────────────────────────────────

class PermissaoIsAlunoTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.aluno_user = make_usuario("A", "a@a.com", "aluno")
        self.empresa_user = make_usuario("E", "e@e.com", "empresa")

    def test_aluno_permitido(self):
        req = self.factory.post("/fake/")
        req.user = self.aluno_user
        self.assertTrue(IsAluno().has_permission(req, None))

    def test_empresa_negada(self):
        req = self.factory.post("/fake/")
        req.user = self.empresa_user
        self.assertFalse(IsAluno().has_permission(req, None))


class PermissaoIsEmpresaTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.empresa_user = make_usuario("E", "emp@e.com", "empresa")
        self.aluno_user = make_usuario("A", "al@a.com", "aluno")

    def test_empresa_permitida(self):
        req = self.factory.post("/fake/")
        req.user = self.empresa_user
        self.assertTrue(IsEmpresa().has_permission(req, None))

    def test_aluno_negado(self):
        req = self.factory.post("/fake/")
        req.user = self.aluno_user
        self.assertFalse(IsEmpresa().has_permission(req, None))


class PermissaoIsEmpresaUserOnlyTest(TestCase):
    """Compatibilidade com testes existentes (não modificar os originais)."""

    def setUp(self):
        self.factory = APIRequestFactory()
        self.empresa_user = make_usuario("E2", "e2@e.com", "empresa")
        self.aluno_user = make_usuario("A2", "a2@a.com", "aluno")

    def test_empresa_permitida(self):
        req = self.factory.get("/fake/")
        req.user = self.empresa_user
        self.assertTrue(IsEmpresaUserOnly().has_permission(req, None))

    def test_aluno_negado(self):
        req = self.factory.get("/fake/")
        req.user = self.aluno_user
        self.assertFalse(IsEmpresaUserOnly().has_permission(req, None))


class PermissaoAdminOrReadOnlyTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.admin = make_usuario("Admin", "adm@a.com", "coordenador", is_staff=True)
        self.user = make_usuario("User", "u@u.com", "aluno")

    def test_leitura_autenticada_permitida(self):
        req = self.factory.get("/fake/")
        req.user = self.user
        self.assertTrue(IsAdminOrReadOnly().has_permission(req, None))

    def test_escrita_nao_admin_negada(self):
        req = self.factory.post("/fake/")
        req.user = self.user
        self.assertFalse(IsAdminOrReadOnly().has_permission(req, None))

    def test_escrita_admin_permitida(self):
        req = self.factory.post("/fake/")
        req.user = self.admin
        self.assertTrue(IsAdminOrReadOnly().has_permission(req, None))


# ─────────────────────────────────────────────
# 3. CANDIDATURAS
# ─────────────────────────────────────────────

class CandidaturaTest(TestCase):
    def setUp(self):
        self.admin = make_usuario("Admin", "adm@c.com", "coordenador", is_staff=True)

        self.u_aluno = make_usuario("Aluno", "aluno@c.com", "aluno")
        self.u_empresa = make_usuario("Empresa", "empresa@c.com", "empresa")

        self.aluno = Aluno.objects.create(
            usuario=self.u_aluno, matricula="MAT001", curso="Eng. Comp.", periodo=4
        )
        self.empresa = Empresa.objects.create(
            usuario=self.u_empresa, cnpj="00.000.000/0001-00"
        )
        self.vaga = Vaga.objects.create(
            empresa=self.empresa,
            titulo="Dev Backend",
            descricao="Django dev",
            area="TI",
            carga_horaria=20,
            ativa=True,
        )

    def test_aluno_pode_criar_candidatura(self):
        client = jwt_client(self.u_aluno)
        resp = client.post("/api/candidaturas/", {
            "aluno": self.aluno.id,
            "vaga": self.vaga.id
        })
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(resp.data["status"], "pendente")

    def test_empresa_nao_pode_criar_candidatura(self):
        client = jwt_client(self.u_empresa)
        resp = client.post("/api/candidaturas/", {
            "aluno": self.aluno.id,
            "vaga": self.vaga.id
        })
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

    def test_candidatura_duplicada_retorna_400(self):
        Candidatura.objects.create(aluno=self.aluno, vaga=self.vaga)
        client = jwt_client(self.u_aluno)
        resp = client.post("/api/candidaturas/", {
            "aluno": self.aluno.id,
            "vaga": self.vaga.id
        })
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_admin_pode_aceitar_candidatura(self):
        cand = Candidatura.objects.create(aluno=self.aluno, vaga=self.vaga)
        client = jwt_client(self.admin)
        resp = client.patch(f"/api/candidaturas/{cand.id}/aceitar/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data["status"], "aceita")

    def test_aceitar_candidatura_cria_estagio(self):
        cand = Candidatura.objects.create(aluno=self.aluno, vaga=self.vaga)
        client = jwt_client(self.admin)
        client.patch(f"/api/candidaturas/{cand.id}/aceitar/")
        self.assertTrue(Estagio.objects.filter(aluno=self.aluno, vaga=self.vaga).exists())

    def test_admin_pode_rejeitar_candidatura(self):
        cand = Candidatura.objects.create(aluno=self.aluno, vaga=self.vaga)
        client = jwt_client(self.admin)
        resp = client.patch(f"/api/candidaturas/{cand.id}/rejeitar/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data["status"], "rejeitada")

    def test_aceitar_candidatura_ja_aceita_retorna_400(self):
        cand = Candidatura.objects.create(aluno=self.aluno, vaga=self.vaga, status="aceita")
        client = jwt_client(self.admin)
        resp = client.patch(f"/api/candidaturas/{cand.id}/aceitar/")
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_nao_admin_nao_pode_aceitar_candidatura(self):
        cand = Candidatura.objects.create(aluno=self.aluno, vaga=self.vaga)
        client = jwt_client(self.u_aluno)
        resp = client.patch(f"/api/candidaturas/{cand.id}/aceitar/")
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)


# ─────────────────────────────────────────────
# 4. FILTROS DE VAGAS E CANDIDATURAS
# ─────────────────────────────────────────────

class FiltroVagaTest(TestCase):
    def setUp(self):
        self.u_empresa = make_usuario("Emp", "emp@f.com", "empresa")
        self.empresa = Empresa.objects.create(
            usuario=self.u_empresa, cnpj="11.111.111/0001-11"
        )
        Vaga.objects.create(empresa=self.empresa, titulo="Dev Python", descricao="x",
                            area="TI", carga_horaria=20, ativa=True)
        Vaga.objects.create(empresa=self.empresa, titulo="Designer", descricao="x",
                            area="Design", carga_horaria=30, ativa=False)
        Vaga.objects.create(empresa=self.empresa, titulo="Dev Java", descricao="x",
                            area="TI", carga_horaria=40, ativa=True)

        self.user = make_usuario("U", "u@f.com", "aluno")
        self.client = jwt_client(self.user)

    def test_filtro_por_area(self):
        resp = self.client.get("/api/vagas/?area=TI")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 2)

    def test_filtro_por_ativa(self):
        resp = self.client.get("/api/vagas/?ativa=True")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        for v in resp.data:
            self.assertTrue(v["ativa"])

    def test_filtro_por_carga_horaria(self):
        resp = self.client.get("/api/vagas/?carga_horaria=30")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 1)

    def test_filtro_por_empresa(self):
        resp = self.client.get(f"/api/vagas/?empresa={self.empresa.id}")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 3)


class FiltroCandidaturaTest(TestCase):
    def setUp(self):
        self.u_aluno = make_usuario("Al", "al@f.com", "aluno")
        self.u_empresa = make_usuario("Ep", "ep@f.com", "empresa")
        self.aluno = Aluno.objects.create(
            usuario=self.u_aluno, matricula="MAT999", curso="Eng.", periodo=2
        )
        self.empresa = Empresa.objects.create(
            usuario=self.u_empresa, cnpj="22.222.222/0001-22"
        )
        self.vaga1 = Vaga.objects.create(empresa=self.empresa, titulo="V1",
                                         descricao="x", area="TI", carga_horaria=20)
        self.vaga2 = Vaga.objects.create(empresa=self.empresa, titulo="V2",
                                         descricao="x", area="TI", carga_horaria=20)
        Candidatura.objects.create(aluno=self.aluno, vaga=self.vaga1, status="pendente")
        Candidatura.objects.create(aluno=self.aluno, vaga=self.vaga2, status="aceita")

        self.admin = make_usuario("Admin", "adm2@f.com", "coordenador", is_staff=True)
        self.client = jwt_client(self.admin)

    def test_filtro_por_aluno(self):
        resp = self.client.get(f"/api/candidaturas/?aluno={self.aluno.id}")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 2)

    def test_filtro_por_status(self):
        resp = self.client.get("/api/candidaturas/?status=aceita")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        for c in resp.data:
            self.assertEqual(c["status"], "aceita")

    def test_filtro_por_vaga(self):
        resp = self.client.get(f"/api/candidaturas/?vaga={self.vaga1.id}")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 1)


# ─────────────────────────────────────────────
# 5. TESTES DE INTEGRAÇÃO — FLUXOS COMPLETOS
# ─────────────────────────────────────────────

class FluxoCandidaturaCompletaTest(TestCase):
    """
    Fluxo E2E: empresa cria vaga → aluno se candidata →
    admin aceita → estágio criado com status 'pendente'.
    """

    def setUp(self):
        self.admin = make_usuario("Admin", "adm@int.com", "coordenador", is_staff=True)

        self.u_empresa = make_usuario("Empresa Int", "emp@int.com", "empresa")
        self.empresa = Empresa.objects.create(
            usuario=self.u_empresa, cnpj="33.333.333/0001-33"
        )

        self.u_aluno = make_usuario("Aluno Int", "alu@int.com", "aluno")
        self.aluno = Aluno.objects.create(
            usuario=self.u_aluno, matricula="INT001", curso="Eng. Comp.", periodo=3
        )

    def test_fluxo_completo(self):
        # 1) Empresa cria vaga
        client_emp = jwt_client(self.u_empresa)
        resp = client_emp.post("/api/vagas/", {
            "empresa": self.empresa.id,
            "titulo": "Estágio Backend",
            "descricao": "Django + DRF",
            "area": "TI",
            "carga_horaria": 20,
            "ativa": True,
        })
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        vaga_id = resp.data["id"]

        # 2) Aluno se candidata
        client_alu = jwt_client(self.u_aluno)
        resp = client_alu.post("/api/candidaturas/", {
            "aluno": self.aluno.id,
            "vaga": vaga_id,
        })
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        cand_id = resp.data["id"]

        # 3) Admin aceita candidatura
        client_adm = jwt_client(self.admin)
        resp = client_adm.patch(f"/api/candidaturas/{cand_id}/aceitar/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data["status"], "aceita")

        # 4) Estágio foi criado
        estagio = Estagio.objects.filter(aluno=self.aluno, vaga_id=vaga_id).first()
        self.assertIsNotNone(estagio)
        self.assertEqual(estagio.status, "pendente")


class FluxoRejeicaoTest(TestCase):
    """Fluxo de rejeição: aluno candidata → admin rejeita → estágio NÃO criado."""

    def setUp(self):
        self.admin = make_usuario("Adm", "adm@rej.com", "coordenador", is_staff=True)
        u_emp = make_usuario("Emp", "emp@rej.com", "empresa")
        empresa = Empresa.objects.create(usuario=u_emp, cnpj="44.444.444/0001-44")
        self.vaga = Vaga.objects.create(empresa=empresa, titulo="Vaga R",
                                        descricao="x", area="TI", carga_horaria=20)
        u_alu = make_usuario("Alu", "alu@rej.com", "aluno")
        self.aluno = Aluno.objects.create(
            usuario=u_alu, matricula="REJ001", curso="Eng.", periodo=1
        )
        self.cand = Candidatura.objects.create(aluno=self.aluno, vaga=self.vaga)

    def test_rejeicao_nao_cria_estagio(self):
        client = jwt_client(self.admin)
        resp = client.patch(f"/api/candidaturas/{self.cand.id}/rejeitar/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertFalse(Estagio.objects.filter(aluno=self.aluno).exists())
