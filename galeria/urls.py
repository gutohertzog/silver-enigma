from django.urls import path
from galeria.views import view_index, view_busca, view_imagens

app_name = 'galeria'

urlpatterns = [
    path('', view_index, name='index'),
    path('imagens/', view_imagens, name='imagens'),
    path('busca/', view_busca, name='busca'),
]

