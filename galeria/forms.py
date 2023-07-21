from django import forms
from galeria.models import Imagem

class ImagemForm(forms.ModelForm):
    class Meta:
        model = Imagem
        # fields # para mostrar apenas pontualmente
        exclude = ['eh_publicada',]

        widgets = {
            'nome':forms.TextInput(),
            'legenda': forms.TextInput(),
            'categoria': forms.Select(),
            'descricao': forms.Textarea(),
            'foto': forms.FileInput(),
            'data_fotografia': forms.DateInput(
                format = '%d/%m/%Y',
                attrs = {
                    'type': 'date',
                }
            ),
            'usuario': forms.Select(),
        }

        labels = {
            'descricao': 'Descrição',
            'data_fotografia': 'data da Foto',
            'usuario': 'Usuário'
        }

