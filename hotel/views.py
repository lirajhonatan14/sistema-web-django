from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ReservaDayForm, Reservaform
from datetime import datetime, date
from .models import Reserva, ReservaServicoAdicional
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Reserva, ReservaDay
from django.views.generic import View
from django.core.exceptions import ValidationError

@login_required(login_url="/auth/login/")
# views.py
def nova_reserva(request):
    if request.method == 'POST':
        form_reserva = Reservaform(request.POST)
        if form_reserva.is_valid():
            reserva = form_reserva.save(commit=False)
            reserva.usuario = request.user
            reserva.save()
            form_reserva.save_m2m()
            return redirect('home')
    else:
        form_reserva = Reservaform()
    return render(request, 'reserva.html', {'form_reserva': form_reserva})






    
@login_required(login_url="/auth/login/")
def reservaday(request):
    if request.method == 'POST':
        form_reserva = ReservaDayForm(request.POST)
        if form_reserva.is_valid():
            reserva = form_reserva.save(commit=False)
            reserva.usuario = request.user
<<<<<<< HEAD
=======
            pacote = reserva.pacote
            if pacote:
                reserva.dias_utilizados = pacote.quantidade_dias
>>>>>>> 1e0f72eb25cb8cf64458f5b391e22ffc0920abd6
            reserva.save()
            form_reserva.save_m2m()
            return redirect('home')
    else:
        form_reserva = ReservaDayForm()
    return render(request, 'reserva_day.html', {'form_reserva': form_reserva})


<<<<<<< HEAD
=======


>>>>>>> 1e0f72eb25cb8cf64458f5b391e22ffc0920abd6
@login_required(login_url="/auth/login/")
def reserva_list(request):
    hoje = date.today()  # obtém a data atual
    reservas = Reserva.objects.filter(pago=False)
<<<<<<< HEAD

    context = {
        'reservas': reservas
=======
    cont = reservas.count()
    context = {
        'reservas': reservas,
        'cont':cont,
>>>>>>> 1e0f72eb25cb8cf64458f5b391e22ffc0920abd6
    }
    return render(request, 'lista_reservas.html', context)

@login_required(login_url="/auth/login/")
def reservaday_list(request):
    hoje = date.today()  # obtém a data atual
    reservas = ReservaDay.objects.filter(pago=False)
<<<<<<< HEAD

    context = {
        'reservas': reservas
=======
    cont = reservas.count()

    context = {
        'cont':cont,
        'reservas': reservas,
>>>>>>> 1e0f72eb25cb8cf64458f5b391e22ffc0920abd6
    }
    return render(request, 'lista_reservasday.html', context)


@login_required(login_url="/auth/login/")
def proc_reserva(request):
    hoje = date.today()  # obtém a data atual
    reservas = Reserva.objects.all()

    context = {
        'reservas': reservas
    }
    return render(request, 'historico_reserva.html', context)


def puxar_reserva(request):
    if request.method == 'POST':
        return redirect('mostrar_reserva')
        
    animais = Reserva.objects.all()
    return render(request, 'procurar_reserva.html', {'animais': animais})



def mostrar_reserva(request):
    nome_id = request.POST.get('nome_id')
    try:
        animal = Reserva.objects.get(num_reserva=nome_id)
    except Reserva.DoesNotExist:
        # Lógica de tratamento caso o animal não seja encontrado
        return HttpResponse("Reserva não encontrada")
    else:
        # Lógica para exibir a ficha do animal
        return render(request, 'mostrar_reserva.html', {'animal': animal})
    
def puxar_reservaday(request):
    if request.method == 'POST':
        return redirect('mostrar_reservaday')
        
    animais = ReservaDay.objects.all()
    return render(request, 'procurar_reservaday.html', {'animais': animais})



def mostrar_reservaday(request):
    nome_id = request.POST.get('nome_id')
    try:
        animal = ReservaDay.objects.get(num_reserva=nome_id)
    except ReservaDay.DoesNotExist:
        # Lógica de tratamento caso o animal não seja encontrado
        return HttpResponse("Reserva não encontrada")
    else:
        # Lógica para exibir a ficha do animal
        return render(request, 'mostrar_reservaday.html', {'animal': animal})




