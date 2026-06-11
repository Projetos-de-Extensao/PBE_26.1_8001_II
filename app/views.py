from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from .models import (
    Usuario,
    Aluno,
    Professor,
    Coordenador,
    Empresa,
    Vaga,
    Candidatura,
    Estagio,
    Documento,
    Relatorio
)

from .serializers import (
    UsuarioSerializer,
    AlunoSerializer,
    ProfessorSerializer,
    CoordenadorSerializer,
    EmpresaSerializer,
    VagaSerializer,
    CandidaturaSerializer,
    EstagioSerializer,
    DocumentoSerializer,
    RelatorioSerializer
)

from .permissions import IsAdminOrReadOnly, IsAdminUserOnly, IsAluno, IsEmpresa


def home(request):
    return HttpResponse("""
        <h1>Sistema de Gestão de Estágios</h1>

        <p>
            API REST desenvolvida para gerenciamento de estágios,
            permitindo controle de usuários, vagas, candidaturas,
            documentos e acompanhamento institucional.
        </p>

        <h2>Funcionalidades</h2>

        <ul>
            <li>Cadastro de alunos</li>
            <li>Cadastro de empresas</li>
            <li>Gerenciamento de vagas</li>
            <li>Candidatura de alunos às vagas</li>
            <li>Controle de estágios</li>
            <li>Envio de documentos</li>
            <li>Geração de relatórios</li>
        </ul>

        <h2>Acessos</h2>

        <ul>
            <li><a href="/api/">API REST</a></li>
            <li><a href="/admin/">Painel Administrativo</a></li>
            <li><a href="/api/usuarios/">Usuários</a></li>
            <li><a href="/api/alunos/">Alunos</a></li>
            <li><a href="/api/empresas/">Empresas</a></li>
            <li><a href="/api/vagas/">Vagas</a></li>
            <li><a href="/api/candidaturas/">Candidaturas</a></li>
            <li><a href="/api/estagios/">Estágios</a></li>
            <li><a href="/api/documentos/">Documentos</a></li>
            <li><a href="/api/relatorios/">Relatórios</a></li>
        </ul>
    """)


def empresa_dashboard(request):
    if not request.user or not request.user.is_authenticated:
        return HttpResponse("Acesso não autorizado", status=401)

    if getattr(request.user, "perfil", None) != "empresa":
        return HttpResponse("Acesso negado", status=403)

    empresa = Empresa.objects.filter(usuario=request.user).first()
    if not empresa:
        return HttpResponse("Empresa não encontrada", status=404)

    vagas = Vaga.objects.filter(empresa=empresa)

    return render(request, "app/empresa_dashboard.html", {"empresa": empresa, "vagas": vagas})


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAdminOrReadOnly]


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    permission_classes = [IsAdminOrReadOnly]


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [IsAdminOrReadOnly]


class CoordenadorViewSet(viewsets.ModelViewSet):
    queryset = Coordenador.objects.all()
    serializer_class = CoordenadorSerializer
    permission_classes = [IsAdminOrReadOnly]


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [IsAdminOrReadOnly]


class VagaViewSet(viewsets.ModelViewSet):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer

    def get_permissions(self):
        if self.action == "create":
            return [IsEmpresa()]

        return [IsAdminOrReadOnly()]

    def get_queryset(self):
        queryset = Vaga.objects.all()

        area = self.request.query_params.get("area")
        carga_horaria = self.request.query_params.get("carga_horaria")
        empresa = self.request.query_params.get("empresa")
        ativa = self.request.query_params.get("ativa")

        if area:
            queryset = queryset.filter(area__icontains=area)

        if carga_horaria:
            queryset = queryset.filter(carga_horaria=carga_horaria)

        if empresa:
            queryset = queryset.filter(empresa=empresa)

        if ativa:
            queryset = queryset.filter(ativa=ativa)

        return queryset


class CandidaturaViewSet(viewsets.ModelViewSet):
    queryset = Candidatura.objects.all()
    serializer_class = CandidaturaSerializer

    def get_permissions(self):
        if self.action == "create":
            return [IsAluno()]

        if self.action in ["aceitar", "rejeitar", "update", "partial_update", "destroy"]:
            return [IsAdminUserOnly()]

        return [IsAuthenticated()]

    def get_queryset(self):
        queryset = Candidatura.objects.all()

        aluno = self.request.query_params.get("aluno")
        vaga = self.request.query_params.get("vaga")
        status_candidatura = self.request.query_params.get("status")

        if aluno:
            queryset = queryset.filter(aluno=aluno)

        if vaga:
            queryset = queryset.filter(vaga=vaga)

        if status_candidatura:
            queryset = queryset.filter(status=status_candidatura)

        return queryset

    @action(detail=True, methods=["patch"])
    @extend_schema(
        summary="Aceitar candidatura",
        description="Aceita uma candidatura pendente e cria um estágio associado.",
    )
    def aceitar(self, request, pk=None):
        candidatura = self.get_object()

        if candidatura.status != "pendente":
            return Response(
                {"erro": "Apenas candidaturas pendentes podem ser aceitas."},
                status=status.HTTP_400_BAD_REQUEST
            )

        candidatura.status = "aceita"
        candidatura.save()

        Estagio.objects.create(
            aluno=candidatura.aluno,
            vaga=candidatura.vaga,
            status="pendente"
        )

        serializer = self.get_serializer(candidatura)
        return Response(serializer.data)

    @action(detail=True, methods=["patch"])
    @extend_schema(
        summary="Rejeitar candidatura",
        description="Rejeita uma candidatura pendente sem criar estágio.",
    )
    def rejeitar(self, request, pk=None):
        candidatura = self.get_object()

        if candidatura.status != "pendente":
            return Response(
                {"erro": "Apenas candidaturas pendentes podem ser rejeitadas."},
                status=status.HTTP_400_BAD_REQUEST
            )

        candidatura.status = "rejeitada"
        candidatura.save()

        serializer = self.get_serializer(candidatura)
        return Response(serializer.data)


class EstagioViewSet(viewsets.ModelViewSet):
    queryset = Estagio.objects.all()
    serializer_class = EstagioSerializer
    permission_classes = [IsAdminOrReadOnly]


class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    permission_classes = [IsAdminOrReadOnly]


class RelatorioViewSet(viewsets.ModelViewSet):
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer
    permission_classes = [IsAdminOrReadOnly]