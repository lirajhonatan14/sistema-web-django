from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'ficha'
urlpatterns = [
    path('novopet/', views.ficha, name='ficha'),
    path('listapet/', views.lista_fichas_cachorros, name='lista'),
    path('procurar_ficha/', views.puxar_ficha, name='puxar_ficha'),
    path('mostrar_ficha/', views.mostrar_ficha, name='mostrar_ficha'),
] 
    

