from django.contrib import admin
from .models import *

class detUsuarios(admin.ModelAdmin):
    list_display = ('id','nome', 'email', 'fone', 'ativo', 'foto', 'cpf', 'dtNascimento')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

class detMaterias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cargaHoraria', 'periodo', 'ativa')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

class detFilmes(admin.ModelAdmin):
    list_display = ('id','nome', 'categoria_id')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

class detCategoria(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

class detAssinatura(admin.ModelAdmin):
    list_display = ('id', 'nome','valor')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10


class detFavoritos(admin.ModelAdmin):
    list_display = ('id', 'filme_id', 'usuarios_id')
    list_display_links = ('id',)
    list_per_page = 10


admin.site.register(Filmes, detFilmes)
admin.site.register(Categoria, detCategoria)
admin.site.register(Assinatura, detAssinatura)
admin.site.register(Usuarios, detUsuarios)
admin.site.register(Favoritos, detFavoritos)
admin.site.register(Materias, detMaterias)