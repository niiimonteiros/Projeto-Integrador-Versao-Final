from django.shortcuts import render
from django.http import HttpResponse
from .models import DadosTurma


def home(request):
    return render(request,'todos/home.html')


def lista_de_dados(request):
    dados = [
        {"codigosubtipoatividade": 11, "horario": "13 às 14", "diasemana": "4a e 6a", "idade": "acima de 15 anos", "codigoinstrutor": 1.111, "numerovagas": 100},
        {"codigosubtipoatividade": 12, "horario": "8:30 às 9:30", "diasemana": "3a e 5a", "idade": "de 9 a 12 anos", "codigoinstrutor": 1.112, "numerovagas": 12},
        ]
    return render(request, 'todos/TabelaDeAtividades.html', {'dados': dados})

