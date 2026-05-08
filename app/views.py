from django.shortcuts import render
from .models import Produto


def home(request):
    produtos = Produto.objects.filter(disponivel=True)[:6]
    return render(request, "app/home.html", {"produtos": produtos})
