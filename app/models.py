from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    descricao = models.TextField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Usuario(models.Model):

    PERFIL_CHOICES = [
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
        ('coordenador', 'Coordenador'),
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    perfil = models.CharField(max_length=20, choices=PERFIL_CHOICES)

    def login(self):
        print(f"Usuário {self.nome} entrou no sistema.")

    def logout(self):
        print(f"Usuário {self.nome} saiu do sistema.")

    def recuperar_senha(self):
        print(f"E-mail de recuperação enviado para: {self.email}")

    def __str__(self):
        return f"{self.nome} ({self.perfil})"


class Aluno(models.Model):

    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=20)
    curso = models.CharField(max_length=100)

    def cadastrar_estagio(self, nome_empresa):
        print(f"Aluno {self.usuario.nome} cadastrou estágio na empresa: {nome_empresa}")

    def __str__(self):
        return f"{self.usuario.nome} - {self.matricula}"