from django.contrib import admin
from .models import  Contato

# Register your models here.
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'email', 'data_nascimento', 'telefone')


admin.site.register(Contato, ContatoAdmin)
