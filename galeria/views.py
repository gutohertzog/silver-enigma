from django.shortcuts import render
from galeria.models import Imagem

def view_index(request):
    return render(request, 'galeria/paginas/index.html', context={})

def view_imagens(request):
    imagens = Imagem.objects.all()
    return render(request, 'galeria/paginas/imagens.html', context={'imagens':imagens})

def view_busca(request):
    imagens = Imagem.objects.all()

    if 'buscando' in request.GET:
        nome = request.GET['buscando']
        if nome:
            imagens = imagens.filter(nome__icontains=nome)

    return render(request, 'galeria/paginas/busca.html', context={'imagens':imagens})
