from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
<<<<<<< HEAD
from ficha.models import FichaDog
from datetime import datetime
=======
>>>>>>> 1e0f72eb25cb8cf64458f5b391e22ffc0920abd6

def logout_view(request):
    logout(request)
    return redirect('login')

<<<<<<< HEAD
def lembrardatanasc(mes):
     # Obtenha o número do mês atual
    mes_atual = datetime.now().month

    # Verifique se o mês fornecido é o mês atual ou futuro
    if mes >= mes_atual:
        # Filtrar os cachorros que fazem aniversário no mês fornecido
        cachorros_aniversario = FichaDog.objects.filter(data_de_nascimento__month=mes)
        return cachorros_aniversario
    else:
        return []
def home(request, mes=None):
    if mes is None:
        # Obtenha o mês atual
        mes = datetime.now().month
    proximo_mes = mes + 1 if mes < 12 else 1
    aniversario = FichaDog.objects.filter(data_de_nascimento__month=proximo_mes)
    
    cachorros_aniversario = FichaDog.objects.filter(data_de_nascimento__month=mes)
    if mes == 1:
        mesnome = 'Janeiro'
        proxmes = 'Fevereiro'
    elif mes == 2:
        mesnome = 'Fevereiro'
        proxmes = 'Março'
    elif mes == 3:
        mesnome = 'Março'
        proxmes = 'Abril'
    elif mes == 4:
        mesnome = 'Abril'
        proxmes = 'Maio'
    elif mes == 5:
        mesnome = 'Maio'
        proxmes = 'Junho'
    elif mes == 6:
        mesnome = 'Junho'
        proxmes = 'Julho'
    elif mes == 7:
        mesnome = 'Julho'
        proxmes = 'Agosto'
    elif mes == 8:
        mesnome = 'Agosto'
        proxmes = 'Setembro'
    elif mes == 9:
        mesnome = 'Setembro'
        proxmes = 'Outubro'
    elif mes == 10:
        mesnome = 'Outubro'
        proxmes = 'Novembro'
    elif mes == 11:
        mesnome = 'Novembro'
        proxmes = 'Dezembro'
    elif mes == 12:
        mesnome = 'Dezembro'
        proxmes = 'Janeiro'    
        proxmes = 'Fevereiro'
        proxmes = 'Fevereiro'
    return render(request, 'home.html', {'cachorros_aniversario': cachorros_aniversario, 'mes':mesnome, 'proxmes':proxmes, 'aniversario': aniversario})  

=======
def home(request):
    return render(request,'home.html')
>>>>>>> 1e0f72eb25cb8cf64458f5b391e22ffc0920abd6
