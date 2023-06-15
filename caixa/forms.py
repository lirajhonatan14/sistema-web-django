from django import forms
from .models import Caixa, CaixaDay


class CaixaForm(forms.ModelForm):

    class Meta:
        model = Caixa
        fields = ['relatorio_estadia','desconto', 'metodo_de_pagamento']
        widgets = {
            #'usuario': forms.HiddenInput(),
            #'num_reserva': forms.HiddenInput(),
            'data':forms.HiddenInput(),
            
            'pet': forms.HiddenInput(),
        }
    def save(self, commit=True, usuario=None):
        reserva = super().save(commit=False)
        if usuario:
            reserva.usuario = usuario
        if commit:
            reserva.save()
        return reserva
    
class CaixaDayForm(forms.ModelForm):
    
    class Meta:
        model = CaixaDay
        fields = ['relatorio_estadia','desconto', 'metodo_de_pagamento']
        widgets = {
            #'usuario': forms.HiddenInput(),
            #'num_reserva': forms.HiddenInput(),
            'data':forms.HiddenInput(),
            'pet': forms.HiddenInput(),
<<<<<<< HEAD
=======
            'pacote':forms.HiddenInput(),
>>>>>>> 1e0f72eb25cb8cf64458f5b391e22ffc0920abd6
        }
    def save(self, commit=True, usuario=None):
        reserva = super().save(commit=False)
        if usuario:
            reserva.usuario = usuario
        if commit:
            reserva.save()
        return reserva
    
    

