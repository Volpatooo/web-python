from django import forms

from steamfake.models import Categoria

class JogoForm(forms.Form):
    nome = forms.CharField(
        max_length=50,
        min_length=3,
        label="Nome do Jogo",
        widget=forms.TextInput( # isso serve somente para estilizar os campos de texto
            attrs={
                "class": "input" 
            }
        )
    )
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        empty_label="Selecione a Categoria",
    )
    valor = forms.DecimalField(
        max_digits=9,
        decimal_places=2,
        label="Valor",
        widget=forms.TextInput(
            attrs={
                "class": "input"
            }
        )
    )
    data_lancamento = forms.DateField(
        label="Data de Lançamento",
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "input"
            }
        )
    )
    desenvolvedora = forms.CharField(
        label="Desenvolvedora",
        min_length=2,
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "input"
            }
        )
    )
    descricao = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "textarea"
            }
        )
    ) 
    foto_capa = forms.ImageField(label="Foto de Capa", required=False)


class JogoEditarForm(forms.Form):
    nome = forms.CharField(
        max_length=50,
        min_length=3,
        label="Nome do Jogo",
        widget=forms.TextInput( # isso serve somente para estilizar os campos de texto
            attrs={
                "class": "input" 
            }
        )
    )
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        empty_label="Selecione a Categoria",
    )
    valor = forms.DecimalField(
        max_digits=9,
        decimal_places=2,
        label="Valor",
        widget=forms.TextInput(
            attrs={
                "class": "input"
            }
        )
    )
    data_lancamento = forms.DateField(
        label="Data de Lançamento",
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "input"
            }
        )
    )
    desenvolvedora = forms.CharField(
        label="Desenvolvedora",
        min_length=2,
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "input"
            }
        )
    )
    descricao = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "textarea"
            }
        )
    ) 
    foto_capa = forms.ImageField(label="Foto de Capa", required=False)

