from django.shortcuts import render

# Inclui a classe HttpResponse.
from django.http import HttpResponse


# Define uma function view chamada index.
def index(request):
    return render(request, "index.html", {"título": "Últimos Artigos"})  # Novo returno


# Define uma function view chamada ola.


def ola(request):
    return render(request, "home.html")


from blog.models import Post  # Acrescentar


def ola(request):  # Modificar
    # return HttpResponse('Olá django')
    posts = Post.objects.all()  # recupera todos os posts do banco de dados
    context = {"posts_list": posts}  # cria um dicionário com os dado
    return render(
        request, "posts.html", context
    )  # renderiza o template e passa o contexto
