from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

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


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class CoordenadorViewSet(viewsets.ModelViewSet):
    queryset = Coordenador.objects.all()
    serializer_class = CoordenadorSerializer


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer


class VagaViewSet(viewsets.ModelViewSet):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer

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


class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer


class RelatorioViewSet(viewsets.ModelViewSet):
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer