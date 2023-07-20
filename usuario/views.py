from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from usuario.forms import CadastroForms, UsuarioForm
# from . import forms

def view_login(request):
    formulario = UsuarioForm()

    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)

        if formulario.is_valid():
            nome = formulario['login_nome'].value()
            senha = formulario['login_senha'].value()

            usuario = auth.authenticate(
                request,
                username = nome,
                password = senha
            )

            if usuario is not None:
                print('usuario nao eh None')
                messages.success(request, f'Usuario {nome} entrou com sucesso!')
                auth.login(request, usuario)
                return redirect('galeria:index')
            else:
                messages.error(request, 'usuario ou senha incorretos')
                return redirect('usuario:login')

    return render(request, 'usuario/paginas/login.html', context={'formulario':formulario})

def view_cadastro(request):
    formulario = CadastroForms()

    if request.method == 'POST':
        formulario = CadastroForms(request.POST)

        if formulario.is_valid():
            
            nome = formulario['nome_cadastro'].value()
            email = formulario['email_cadastro'].value()
            senha = formulario['senha_1'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'usuario ja existe')
                return redirect('usuario:cadastro')

            novo_usuario = User.objects.create_user(
                username = nome,
                email = email,
                password = senha
            )
            novo_usuario.save()
            messages.success(request, 'usuario criado!')
            return redirect('usuario:login')

    return render(request, 'usuario/paginas/cadastro.html', context={'formulario':formulario})

def logout(request):
    auth.logout(request)
    messages.success(request, 'usuario deslogado!')
    print('usuario deslogado')
    return redirect('usuario:login')

