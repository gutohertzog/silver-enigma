from django.urls import path
from galeria.views import view_index, view_busca, view_imagens, view_imagem,\
    view_imagem_adiciona, view_imagem_edita, view_imagem_apaga

app_name = 'galeria'

urlpatterns = [
    path('', view_index, name='index'),
    path('imagens/', view_imagens, name='imagens'),
    path('busca/', view_busca, name='busca'),
    path('imagens/imagem/<int:id_url>/', view_imagem),
    path('imagem-adiciona/', view_imagem_adiciona, name='imagem_adiciona'),
    path('imagem-edita/<int:id_url>/', view_imagem_edita, name='imagem_edita'),
    path('imagem-apaga/<int:id_url>/', view_imagem_apaga, name='imagem_apaga'),
]

