from django.contrib import admin
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


admin.site.register(Usuario)
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Coordenador)
admin.site.register(Empresa)
admin.site.register(Vaga)
admin.site.register(Candidatura)
admin.site.register(Estagio)
admin.site.register(Documento)
admin.site.register(Relatorio)