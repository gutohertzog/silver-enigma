from django.shortcuts import render, redirect
from django.contrib import messages
from galeria.models import Imagem

def view_index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado no galeria/index.html')
        return redirect('usuario:login')

    return render(request, 'galeria/paginas/index.html', context={})

def view_imagens(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado no galeria/imagens.html')
        return redirect('usuario:login')

    imagens = Imagem.objects.all()
    return render(request, 'galeria/paginas/imagens.html', context={'imagens':imagens})

def view_imagem(request, id_url):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado no galeria/imagem.html')
        return redirect('usuario:login')

    imagem = Imagem.objects.filter(id=id_url)
    if imagem:
        imagem = imagem[0]
    return render(request, 'galeria/paginas/imagem.html', context={'imagem':imagem})

def view_busca(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado no galeria/busca.html')
        return redirect('usuario:login')

    imagens = Imagem.objects.all()
    print(request)

    if 'buscando' in request.GET:
        nome = request.GET['buscando']
        if nome:
            imagens = imagens.filter(nome__icontains=nome)

    return render(request, 'galeria/paginas/busca.html', context={'imagens':imagens})

