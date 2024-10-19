import os
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render
from steamfake.forms import JogoEditarForm, JogoForm
from steamfake.models import Categoria, Jogo, Tag
from django.conf import settings


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



def jogo_index(request: HttpRequest) -> HttpResponse:
    jogos = Jogo.objects.all()
    return render(request, "jogos/index.html", context={"jogos": jogos})


def jogo_cadastro(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = JogoForm()
        return render(request, "jogos/cadastro.html", context={"form": form})
    else:
        form = JogoForm(request.POST, request.FILES)
        if form.is_valid():
            jogo = Jogo()
            jogo.nome = form.cleaned_data["nome"]
            jogo.descricao = form.cleaned_data["descricao"]
            jogo.valor = form.cleaned_data["valor"]
            jogo.data_lancamento = form.cleaned_data["data_lancamento"]
            jogo.desenvolvedora = form.cleaned_data["desenvolvedora"]
            jogo.categoria = form.cleaned_data["categoria"]
            jogo.foto_capa = form.cleaned_data["foto_capa"]
            jogo.save()
            return redirect("jogos")
        return render(request, "jogos/cadastro.html", context={"form": form})
    

def jogo_apagar(request: HttpRequest, id: int) -> HttpResponse:
    jogo = Jogo.objects.get(pk=id)
    jogo.delete()
    return redirect("jogos")


def jogo_editar(request: HttpRequest, id: int) -> HttpResponse:
    jogo = Jogo.objects.get(pk=id)
    if request.method == "GET":
        form = JogoEditarForm(initial=jogo.__dict__) # traz as informacoes anteriores como estavam e da a opcao para editar
        form.initial["categoria"] = jogo.categoria
        form.initial["data_lancamento"] = jogo.data_lancamento.strftime("%Y-%m-%d") # traz a data de lancamento antiga
        return render(request, "jogos/editar.html", context={"form": form})
    else:
        form = JogoEditarForm(request.POST, request.FILES)
        if form.is_valid():
            jogo.nome = form.cleaned_data["nome"]
            jogo.descricao = form.cleaned_data["descricao"]
            jogo.valor = form.cleaned_data["valor"]
            jogo.data_lancamento = form.cleaned_data["data_lancamento"]
            jogo.desenvolvedora = form.cleaned_data["desenvolvedora"]
            jogo.categoria = form.cleaned_data["categoria"]
            jogo.foto_capa = form.cleaned_data["foto_capa"]
            jogo.save()
            return redirect("jogos")
        return render(request, "jogos/editar.html", context={"form": form})
    
