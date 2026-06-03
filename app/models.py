from django.db import models


class Usuario(models.Model):

    PERFIL_CHOICES = [
        ("aluno", "Aluno"),
        ("professor", "Professor"),
        ("coordenador", "Coordenador"),
        ("empresa", "Empresa"),
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    perfil = models.CharField(max_length=20, choices=PERFIL_CHOICES)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nome", "perfil"]

    def __str__(self):
        return f"{self.nome} ({self.perfil})"

    def set_password(self, raw_password):
        self.senha = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.senha)

    def _senha_esta_hashed(self):
        try:
            identify_hasher(self.senha)
            return True
        except (ValueError, ImproperlyConfigured):
            return False

    def save(self, *args, **kwargs):
        if self.senha and not self._senha_esta_hashed():
            self.senha = make_password(self.senha)
        super().save(*args, **kwargs)


class Aluno(models.Model):

    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=20, unique=True)
    curso = models.CharField(max_length=100)
    periodo = models.IntegerField()

    def __str__(self):
        return f"{self.usuario.nome} - {self.matricula}"


class Professor(models.Model):

    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    area_atuacao = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario.nome


class Coordenador(models.Model):

    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    curso_coordenado = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario.nome


class Empresa(models.Model):

    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=18, unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    endereco = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.usuario.nome


class Vaga(models.Model):

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    area = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class Candidatura(models.Model):

    STATUS_CHOICES = [
        ("pendente", "Pendente"),
        ("aceita", "Aceita"),
        ("rejeitada", "Rejeitada"),
    ]

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pendente"
    )

    data_candidatura = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ("aluno", "vaga")

    def __str__(self):
        return f"{self.aluno.usuario.nome} - {self.vaga.titulo} ({self.status})"


class Estagio(models.Model):

    STATUS_CHOICES = [
        ("pendente", "Pendente"),
        ("aprovado", "Aprovado"),
        ("reprovado", "Reprovado"),
        ("concluido", "Concluído"),
    ]

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)

    professor = models.ForeignKey(
        Professor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    coordenador = models.ForeignKey(
        Coordenador,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pendente"
    )

    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.aluno.usuario.nome} - {self.vaga.titulo}"


class Documento(models.Model):

    TIPO_CHOICES = [
        ("termo", "Termo de Compromisso"),
        ("apolice", "Apólice"),
        ("relatorio_parcial", "Relatório Parcial"),
        ("relatorio_final", "Relatório Final"),
    ]

    STATUS_CHOICES = [
        ("pendente", "Pendente"),
        ("aprovado", "Aprovado"),
        ("rejeitado", "Rejeitado"),
    ]

    estagio = models.ForeignKey(Estagio, on_delete=models.CASCADE)

    tipo = models.CharField(
        max_length=30,
        choices=TIPO_CHOICES
    )

    arquivo = models.FileField(
        upload_to="documentos/",
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pendente"
    )

    data_envio = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {self.estagio.aluno.usuario.nome}"


class Relatorio(models.Model):

    estagio = models.ForeignKey(Estagio, on_delete=models.CASCADE)

    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo