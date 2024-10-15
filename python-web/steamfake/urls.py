from django.urls import path
from steamfake import views

urlpatterns = [
    path("categoria", views.categoria_index, name="categorias"), # no caminho categoria chamamos a função categoria_index
    path("categoria/cadastro", views.categoria_cadastro), # no caminho categoria/cadastro chamamos a funcao categoria.cadastro
    path("categoria/cadastrar", views.categoria_cadastrar),
    path("categoria/apagar/<int:id>", views.categoria_apagar),
]
