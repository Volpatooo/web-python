from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
# request -> requisicao que é feita no navegador para o back-end
# response -> resposta que o back-end devolve para o navegador

def index(request: HttpRequest) -> HttpResponse:
    # obteve o arquivo html que esta dentro da pasta templates e armazena ná variavel template
    template = loader.get_template(template_name='index.html')
    # Renderizar o template armazenado na variavel html ou seja vai gerar o html
    html = template.render(context={}, request=request)
    # instanciando um objeto da classe HttpResponse definindo o que será retornado da req
    response = HttpResponse(content=html)
    return response


def contato(request: HttpRequest) -> HttpResponse:
    # # obteve o arquivo html que esta dentro da pasta templates e armazena ná variavel template
    # template = loader.get_template(template_name='contato.html')
    # # Renderizar o template armazenado na variavel html ou seja vai gerar o html
    # html = template.render(context={}, request=request)
    # # instanciando um objeto da classe HttpResponse definindo o que será retornado da req
    # response = HttpResponse(content=html)
    # return response
    return render(request, "contato.html", context={})


def calculadora(request: HttpRequest) -> HttpResponse:
    return render(request, "calculadora.html", context={})


def calcular(request: HttpRequest) -> HttpResponse:
    nmr1 = int(request.GET.get("nmr1"))
    nmr2 = int(request.GET.get("nmr2"))
    soma = nmr1 + nmr2
    dados_para_html = {
        'soma': soma
    }
    return render(request, "resultados.html", context=dados_para_html)
    

