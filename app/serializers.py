from rest_framework import serializers
from .models import Usuario, Aluno, Professor, Coordenador, Empresa, Vaga, Candidatura, Estagio, Documento, Relatorio


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["id", "nome", "email", "perfil"]


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


class CandidaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidatura
        fields = "__all__"

    def validate(self, data):
        aluno = data.get("aluno")
        vaga = data.get("vaga")

        if Candidatura.objects.filter(aluno=aluno, vaga=vaga).exists():
            raise serializers.ValidationError(
                "O aluno já está inscrito nesta vaga."
            )

        return data


class EstagioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estagio
        fields = "__all__"


class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = "__all__"

    def validate_arquivo(self, value):
        extensoes_permitidas = [".pdf", ".doc", ".docx"]
        nome_arquivo = value.name.lower()

        if not any(nome_arquivo.endswith(ext) for ext in extensoes_permitidas):
            raise serializers.ValidationError(
                "Envie apenas arquivos PDF, DOC ou DOCX."
            )

        return value


class RelatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relatorio
        fields = "__all__"