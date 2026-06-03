from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
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
    Relatorio,
)


class UsuarioCreationForm(forms.ModelForm):
    senha1 = forms.CharField(label="Senha", widget=forms.PasswordInput)
    senha2 = forms.CharField(label="Confirme a senha", widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ("email", "nome", "perfil")

    def clean_senha2(self):
        senha1 = self.cleaned_data.get("senha1")
        senha2 = self.cleaned_data.get("senha2")
        if senha1 and senha2 and senha1 != senha2:
            raise forms.ValidationError("As senhas não coincidem.")
        return senha2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["senha1"])
        if commit:
            user.save()
        return user


class UsuarioChangeForm(forms.ModelForm):
    senha = ReadOnlyPasswordHashField(label="Senha")

    class Meta:
        model = Usuario
        fields = "__all__"

    def clean_senha(self):
        return self.initial.get("senha")


class UsuarioAdmin(BaseUserAdmin):
    form = UsuarioChangeForm
    add_form = UsuarioCreationForm

    list_display = ("email", "nome", "perfil", "is_staff")
    list_filter = ("perfil", "is_staff")

    fieldsets = (
        (None, {"fields": ("email", "senha")}),
        ("Personal info", {"fields": ("nome", "perfil")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "is_active")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "nome", "perfil", "senha1", "senha2"),
            },
        ),
    )

    search_fields = ("email", "nome")
    ordering = ("email",)
    filter_horizontal = ()


class AlunoAdmin(admin.ModelAdmin):
    list_display = ("get_nome_usuario", "matricula", "curso", "periodo")
    list_filter = ("curso", "periodo")
    search_fields = ("usuario__nome", "usuario__email", "matricula")
    
    def get_nome_usuario(self, obj):
        return obj.usuario.nome
    get_nome_usuario.short_description = "Aluno"


class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("get_nome_usuario", "area_atuacao")
    list_filter = ("area_atuacao",)
    search_fields = ("usuario__nome", "usuario__email", "area_atuacao")
    
    def get_nome_usuario(self, obj):
        return obj.usuario.nome
    get_nome_usuario.short_description = "Professor"


class CoordenadorAdmin(admin.ModelAdmin):
    list_display = ("get_nome_usuario", "curso_coordenado")
    list_filter = ("curso_coordenado",)
    search_fields = ("usuario__nome", "usuario__email", "curso_coordenado")
    
    def get_nome_usuario(self, obj):
        return obj.usuario.nome
    get_nome_usuario.short_description = "Coordenador"


class EmpresaAdmin(admin.ModelAdmin):
    list_display = ("get_nome_usuario", "cnpj", "telefone")
    list_filter = ("usuario__is_active",)
    search_fields = ("usuario__nome", "usuario__email", "cnpj")
    readonly_fields = ("cnpj",)
    
    def get_nome_usuario(self, obj):
        return obj.usuario.nome
    get_nome_usuario.short_description = "Empresa"


class VagaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "get_empresa", "area", "carga_horaria", "ativa")
    list_filter = ("area", "ativa")
    search_fields = ("titulo", "empresa__usuario__nome", "area")
    
    def get_empresa(self, obj):
        return obj.empresa.usuario.nome
    get_empresa.short_description = "Empresa"


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Coordenador, CoordenadorAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Vaga, VagaAdmin)
admin.site.register(Candidatura)
admin.site.register(Estagio)
admin.site.register(Documento)
admin.site.register(Relatorio)