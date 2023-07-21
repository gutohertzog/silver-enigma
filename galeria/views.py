from django.shortcuts import render, redirect
from django.contrib import messages
from galeria.models import Imagem
from galeria.forms import ImagemForm

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

def view_imagem_adiciona(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado no imagem_adiciona/busca.html')
        return redirect('usuario:login')

    formulario = ImagemForm()
    if request.method == 'POST':
        formulario = ImagemForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Dados salvos com sucesso!')
            return redirect('galeria:index')

    return render(request, 'galeria/paginas/imagem_adiciona.html', context={'formulario':formulario})

def view_imagem_edita(request, id_url):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado no galeria/imagem_edita.html')
        return redirect('usuario:login')

    imagem = Imagem.objects.filter(id=id_url)
    if not imagem:
        messages.error(request, 'imagem nao encontrada')
        return redirect('galeria:imagens')

    imagem = imagem[0]
    formulario = ImagemForm(instance=imagem)

    if request.method == 'POST':
        formulario = ImagemForm(request.POST, request.FILES, instance=imagem)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'dados alterados com sucesso!')
            return redirect('galeria:imagens')

    return render(request, 'galeria/paginas/imagem_edita.html', context={'formulario':formulario, 'id_url':id_url})

def view_imagem_apaga(request, id_url):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado no galeria/imagem_apaga.html')
        return redirect('usuario:login')

    imagem = Imagem.objects.filter(id=id_url)
    if not imagem:
        messages.error(request, 'imagem nao encontrada')
        return redirect('galeria:imagens')

    imagem = imagem[0]
    imagem.delete()

    messages.success(request, 'dados deletados com sucesso!')
    return render(request, 'galeria/paginas/imagem_apaga.html')




