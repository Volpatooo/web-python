from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render
from steamfake.models import Categoria, Tag


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")

def categoria_index(request: HttpRequest) -> HttpResponse:
    categorias = Categoria.objects.all()
    dados = {
        "categorias": categorias
    }
    return render(request, "categorias/index.html", context=dados)



def categoria_cadastro(request: HttpRequest) -> HttpResponse:
    return render(request, "categorias/cadastro.html",)

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


def categoria_editar(request: HttpRequest, id: int) -> HttpResponse:
    # Busca a categoria do banco filtrando por id
    categoria = Categoria.objects.get(pk=id)
    dados = {
        "categoria": categoria
    }
    return render(request, "categorias/editar.html", context=dados)


def categoria_editado(request: HttpRequest, id: int) -> HttpResponse:
    # obter o nome que o ussuario prrencheu na lista
    nome = request.POST.get("nome")
    # passar a catgeoria pelo id
    categoria = Categoria.objects.get(pk=id)
    categoria.nome = nome
    # att a catgeoria na tabela Update categorias set nome = ? where id = ?
    categoria.save()
    # redireciona para a tela de lista das categorias
    return redirect("categorias")


def tag_index(request: HttpRequest) -> HttpResponse:
    tags = Tag.objects.all()
    dados = {
        "tags": tags
    }
    return render(request, "tags/index.html", context=dados)


def tag_cadastro(request: HttpRequest) -> HttpResponse:
    return render(request, "tags/cadastro.html") # tags é o nome da sub pasta


def tag_cadastrar(request: HttpRequest) -> HttpResponse:
    nome = request.POST.get("nome")
    descricao = request.POST.get("descricao")
    tags = Tag(nome=nome, descricao=descricao)
    tags.save()
    return redirect("tags") # aqui e tags pois no tag_index definimos como tags


def tag_apagar(request: HttpRequest, id: int) -> HttpResponse:
    tag = Tag.objects.get(pk=id) # busca a tag no banco filtarndo pelo id
    tag.delete() # apaga a tag selecionada
    return redirect("tags") # retorna a lista de tags


def tag_editar(request: HttpRequest, id: int) -> HttpResponse:
    tag = Tag.objects.get(pk=id)
    dados = {
        "tag": tag
    }
    return render(request, "tags/editar.html", context=dados)


def tag_editado(request: HttpRequest, id: int) -> HttpResponse:
    nome = request.POST.get("nome") # obter o nome que o ususario preencheu na lista
    descricao = request.POST.get("descricao") # obter a descricao que o usuario preencheu na lista
    tag = Tag.objects.get(pk=id) # passar a tag pelo id
    tag.nome = nome
    tag.descricao = descricao
    tag.save()
    return redirect("tags")