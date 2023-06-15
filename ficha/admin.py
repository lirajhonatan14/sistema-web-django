from django.contrib import admin
<<<<<<< HEAD
from .models import FichaDog, Vacina, VacinaAnimal

admin.site.register(FichaDog)
admin.site.register(Vacina)
admin.site.register(VacinaAnimal)

=======
from .models import FichaDog

@admin.register(FichaDog)
class DogAdmin(admin.ModelAdmin):
    list_display = ['nome']
    #list_filter = ('nome')
    #search_fields = ('nome')
>>>>>>> 1e0f72eb25cb8cf64458f5b391e22ffc0920abd6
