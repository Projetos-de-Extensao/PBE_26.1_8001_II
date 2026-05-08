from django.http import HttpResponse


def home(request):
    return HttpResponse("Bem-vindo ao meu site!")
