from django.contrib import admin
from galeria.models import Imagem

class ImagemAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'eh_publicada')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('categoria',)
    list_editable = ('eh_publicada',)
    list_per_page = 10

admin.site.register(Imagem, ImagemAdmin)

