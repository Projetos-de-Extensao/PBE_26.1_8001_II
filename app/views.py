from django.http import HttpResponse
from rest_framework import viewsets
from .models import Usuario, Aluno, Professor, Coordenador, Empresa, Vaga, Estagio, Documento, Relatorio
from .serializers import UsuarioSerializer, AlunoSerializer, ProfessorSerializer, CoordenadorSerializer, EmpresaSerializer, VagaSerializer, EstagioSerializer, DocumentoSerializer, RelatorioSerializer


from django.http import HttpResponse


def home(request):
    return HttpResponse("""
        <h1>Sistema de Gestão de Estágios</h1>

        <p>
            API REST desenvolvida para gerenciamento de estágios,
            permitindo controle de usuários, vagas, documentos
            e acompanhamento institucional.
        </p>

        <h2>Funcionalidades</h2>

        <ul>
            <li>Cadastro de alunos</li>
            <li>Cadastro de empresas</li>
            <li>Gerenciamento de vagas</li>
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


class EstagioViewSet(viewsets.ModelViewSet):
    queryset = Estagio.objects.all()
    serializer_class = EstagioSerializer


class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer


class RelatorioViewSet(viewsets.ModelViewSet):
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer