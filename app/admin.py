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


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Coordenador)
admin.site.register(Empresa)
admin.site.register(Vaga)
admin.site.register(Candidatura)
admin.site.register(Estagio)
admin.site.register(Documento)
admin.site.register(Relatorio)