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

# request.GET é o método da requisição
# request.GET a informação vai na url (https://localhost:8000/sistema/calcular?nmr1=0%nmr2=21)
# request.POST a informação vai por de baixo dos panos (https://localhost:8000/sistema/calcular)
# .get é utilizado para obter um valor nesse caso do html
def calcular(request: HttpRequest) -> HttpResponse:
    nmr1 = int(request.GET.get("nmr1"))
    nmr2 = int(request.GET.get("nmr2"))

    soma = nmr1 + nmr2
    
    if nmr1 > nmr2:
        maior = "primeiro Número"
    else:
        maior = "Número Dois"

    dados_para_html = {
        'soma': soma,
        'maior': maior,
        'nmr1': nmr1,
        'nmr2': nmr2,
    }
    return render(request, "resultados.html", context=dados_para_html)


def aluno(request: HttpRequest) -> HttpResponse:
    return render(request, "aluno.html", context={})

def calcula_media(request: HttpRequest) -> HttpResponse:
    nota1 = float(request.GET.get("nota1").replace(",", "."))
    nota2 = float(request.GET.get("nota2").replace(",", "."))
    nota3 = float(request.GET.get("nota3").replace(",", "."))

    media = (nota1 + nota2 + nota3) / 3

    if media > 7:
        status = "Aluno aprovado"
    elif media < 4:
        status = "Aluno reprovado"
    else:
        status = "Aluno em Exame"
    
    dados_para_html = {
        'media': media, # o que esta entre aspas tem que ser igual ao que esta no resultados.html
        'status': status
    }
    return render(request, "resultados.html", context=dados_para_html)


    

