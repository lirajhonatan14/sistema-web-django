from django.db import models
from hotel.models import Reserva, ReservaDay
from django.contrib.auth.models import User
from ficha.models import FichaDog
from hotel.models import Pacote
import datetime

class Caixa(models.Model):
    num_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE,null=True, blank=True)
    usuario  = models.CharField(max_length=100)
    pet = models.ForeignKey(FichaDog, on_delete=models.CASCADE)
    relatorio_estadia = models.TextField(max_length=500)
    desconto = models.DecimalField(max_digits=3, decimal_places=1)
    METODO_CHOICES = (('Cartão de Crédito', 'Cartão de Crédito'),('Cartão de Debito', 'Cartão de Debito'),('Dinheiro', 'Dinheiro'),('Pix', 'Pix'),)
    metodo_de_pagamento =  models.CharField(max_length=20, choices=METODO_CHOICES)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    data = models.DateField(default=datetime.date.today)
    


    class Meta:
            db_table = 'Caixa'
            
class CaixaDay(models.Model):
    num_reserva = models.ForeignKey(ReservaDay, on_delete=models.CASCADE,null=True, blank=True)
    usuario  = models.CharField(max_length=100)
    pet = models.ForeignKey(FichaDog, on_delete=models.CASCADE)
    relatorio_estadia = models.TextField(max_length=500)
    desconto = models.DecimalField(max_digits=3, decimal_places=1)
    METODO_CHOICES = (('Cartão de Crédito', 'Cartão de Crédito'),('Cartão de Debito', 'Cartão de Debito'),('Dinheiro', 'Dinheiro'),('Pix', 'Pix'),)
    metodo_de_pagamento =  models.CharField(max_length=20, choices=METODO_CHOICES)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    data = models.DateField(default=datetime.date.today)
    pacote = models.ForeignKey(Pacote, on_delete=models.SET_NULL, null=True, blank=True)
    


    class Meta:
            db_table = 'CaixaDay'           

