from rest_framework import serializers
from .models import Usuario, Aluno, Professor, Coordenador, Empresa, Vaga, Estagio, Documento, Relatorio


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = "__all__"


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = "__all__"


class CoordenadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordenador
        fields = "__all__"


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = "__all__"


class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaga
        fields = "__all__"


class EstagioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estagio
        fields = "__all__"


class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = "__all__"


class RelatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relatorio
        fields = "__all__"