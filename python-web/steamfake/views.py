from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render
from steamfake.models import Categoria

# Create your views here.

def categoria_index(request: HttpRequest) -> HttpResponse:
    categorias = Categoria.objects.all()
    dados = {
        "categorias": categorias
    }
    return render(request, "categorias/index.html", context=dados)



def categoria_cadastro(request: HttpRequest) -> HttpResponse:
    return render(request, "categorias/cadastro.html", )

def categoria_cadastrar(request: HttpRequest) -> HttpResponse:
    # obter o nome que o ususario preencheu na tela
    nome = request.POST.get("nome")
    # instanciar um objeto da categoria 
    categoria = Categoria(nome=nome)
    # Persistir a categoria na tabela INSERT INTO (nome) VALUES (?)
    categoria.save()
    # redirecionar para a tela de lista de categorias
    return redirect("categorias")


def categoria_apagar(request: HttpRequest, id: int) -> HttpResponse:
    categoria = Categoria.objects.get(pk=id)
    categoria.delete()
    return redirect("categorias")
