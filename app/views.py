from django.http import HttpResponse
from rest_framework import viewsets
from .models import Usuario, Aluno, Professor, Coordenador, Empresa, Vaga, Estagio, Documento, Relatorio
from .serializers import UsuarioSerializer, AlunoSerializer, ProfessorSerializer, CoordenadorSerializer, EmpresaSerializer, VagaSerializer, EstagioSerializer, DocumentoSerializer, RelatorioSerializer


def home(request):
    return HttpResponse("API do Sistema de Gestão de Estágios")


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