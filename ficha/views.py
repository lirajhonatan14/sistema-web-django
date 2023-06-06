from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DogForm
from django.contrib import messages
from ficha.models import FichaDog
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

@login_required(login_url="/auth/login/")
def ficha(request):
    if request.method == 'POST':
        form = DogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Salvo com sucesso')
            return redirect('reserva')

    else:
        form = DogForm()
    return render(request, 'ficha.html', {'form': form})


@login_required(login_url="/auth/login/")
def lista_fichas_cachorros(request):
    cachorros = FichaDog.objects.all()
    return render(request, 'lista_pet.html', {'cachorros': cachorros})

def puxar_ficha(request):
    if request.method == 'POST':
        return redirect('mostrar_ficha')
        
    animais = FichaDog.objects.all()
    return render(request, 'proc_ficha.html', {'animais': animais})



def mostrar_ficha(request):
    nome_id = request.POST.get('nome_id')
    try:
        animal = FichaDog.objects.get(nome=nome_id)
    except FichaDog.DoesNotExist:
        # Lógica de tratamento caso o animal não seja encontrado
        return HttpResponse("Animal não encontrado")
    else:
        # Lógica para exibir a ficha do animal
        return render(request, 'mostrar_ficha.html', {'animal': animal})
