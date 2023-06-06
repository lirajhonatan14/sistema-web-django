from django import forms
from .models import FichaDog

class DogForm(forms.ModelForm):
    class Meta:
        model = FichaDog
        fields = ['nome', 'raca','data_de_nascimento','sexo', 'peso', 'tipo_alimentacao', 'restricoes_alimentares','nome_tutor','contato_tutor','cpf_tutor','endereco','veterinario', 'observacoes']
        widgets = {
            'data': forms.HiddenInput(),
        }