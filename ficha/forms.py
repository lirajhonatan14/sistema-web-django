from django import forms
<<<<<<< HEAD
from .models import FichaDog, Vacina, VacinaAnimal
=======
from .models import FichaDog
>>>>>>> 1e0f72eb25cb8cf64458f5b391e22ffc0920abd6

class DogForm(forms.ModelForm):
    class Meta:
        model = FichaDog
        fields = ['nome', 'raca','data_de_nascimento','sexo', 'peso', 'tipo_alimentacao', 'restricoes_alimentares','nome_tutor','contato_tutor','cpf_tutor','endereco','veterinario', 'observacoes']
        widgets = {
            'data': forms.HiddenInput(),
<<<<<<< HEAD
        }

class VacinaForm(forms.ModelForm):
    class Meta:
        model = Vacina
        fields = ['nome', 'validade','data_reforco']
        widgets = {
        }
class VacinaAnimalForm(forms.ModelForm):
    class Meta:
        model = VacinaAnimal
        fields = ['pet', 'vacina','data_administracao']
        widgets = {
=======
>>>>>>> 1e0f72eb25cb8cf64458f5b391e22ffc0920abd6
        }