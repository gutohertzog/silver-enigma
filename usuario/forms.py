from django import forms

class UsuarioForm(forms.Form):
    login_nome = forms.CharField(
        label = 'Nome de Login:',
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Ex.: Tom Cruise',
                'class': 'red'
            }
        )
    )

    login_senha = forms.CharField(
        label = 'Senha de Login:',
        required = True,
        max_length = 100,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'Digite sua senha',
            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label = 'Nome de Cadastro',
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Ex.: Tom Cruise',
            }
        )
    )
    email_cadastro = forms.EmailField(
        label = 'Email de Cadastro',
        required = True,
        max_length = 100,
        widget = forms.EmailInput(
            attrs = {
                'placeholder': 'Ex.: tom@cruise.com',
            }
        )
    )
    senha_1 = forms.CharField(
        label = 'Senha de Cadastro',
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'Digite sua senha',
            }
        ),
    )
    senha_2 = forms.CharField(
        label = 'Confirme a Senha',
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'Digite novamente',
            }
        ),
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Espaços não podem!')
            else:
                return nome

    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')

        if senha_1 and senha_2:
            senha_1 = senha_1.strip()
            senha_2 = senha_2.strip()

            if senha_1 != senha_2:
                raise forms.ValidationError('As senhas não são iguais!')
            else:
                return senha_2

