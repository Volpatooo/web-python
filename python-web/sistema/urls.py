# urlpatterns é utilizado para definir quais serão as rotas
# rota é o caminho para poder chegar a função
from django.urls import path
from sistema import views # importou a função index do arquivo views


urlpatterns = [
    # quando o usuario acessar /home será executado a função index, contato que esta dentro do arquivo views.py
    path("/home", views.index),
    path('/', views.index),
    path('/contato', views.contato),
    path('/calculadora', views.calculadora),
    path('/calcular', views.calcular)
]
