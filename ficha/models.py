from django.db import models

class FichaDog(models.Model):
    nome = models.CharField(max_length=100, primary_key=True)
    raca = models.CharField(max_length=100)
    data_de_nascimento =  models.DateField()
    sexo = models.CharField(max_length=1, choices=(('M', 'Macho'), ('F', 'Fêmea')))
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    tipo_alimentacao = models.CharField(max_length=100)
    restricoes_alimentares = models.CharField(max_length=100, blank=True, null=True)
    nome_tutor = models.CharField(max_length=100,blank=True)
    contato_tutor = models.CharField(max_length=100)
    cpf_tutor = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100,blank=True, null=True)
    veterinario = models.CharField(max_length=100,blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)
    
   
    
    class Meta:
            db_table = 'Ficha_Dog'
            
    def __str__(self):
        return f"{self.nome} - {self.raca}"


