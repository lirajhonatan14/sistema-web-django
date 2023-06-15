from django.contrib import admin
from django.urls import path,include
from caixa import views as vw
from . import views
from hotel.views import nova_reserva
from django.views.generic import TemplateView


urlpatterns = [
        path('novareserva/', nova_reserva, name='reserva'), 
        path('novareservaday/', views.reservaday, name='reservaday'),
        path('lista_reservas/', views.reserva_list, name='lista_reserva'),
        path('lista_reservasday/', views.reservaday_list, name='lista_reservaday'),
        path('procurar_reserva/', views.puxar_reserva, name='puxar_reserva'),
        path('mostrar_reserva/', views.mostrar_reserva, name='mostrar_reserva'),
        path('historico_reservas/', views.proc_reserva, name='historico_reserva'),
        path('procurar_reservaday/', views.puxar_reservaday, name='puxar_reservaday'),
        path('mostrar_reservaday/', views.mostrar_reservaday, name='mostrar_reservaday'),
        
    ]
