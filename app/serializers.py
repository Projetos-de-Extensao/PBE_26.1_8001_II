from rest_framework import serializers
from .models import Usuario, Aluno, Professor, Coordenador, Empresa, Vaga, Candidatura, Estagio, Documento, Relatorio


class UsuarioSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True, required=False, min_length=8)

    class Meta:
        model = Usuario
        fields = ["id", "nome", "email", "perfil", "senha"]

    def validate(self, data):
        if self.instance is None and not data.get("senha"):
            raise serializers.ValidationError({"senha": "Este campo é obrigatório."})
        return data

    def create(self, validated_data):
        senha = validated_data.pop("senha", None)
        usuario = Usuario(**validated_data)
        if senha is not None:
            usuario.set_password(senha)
        usuario.save()
        return usuario

    def update(self, instance, validated_data):
        senha = validated_data.pop("senha", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if senha is not None:
            instance.set_password(senha)
        instance.save()
        return instance


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