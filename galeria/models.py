from django.db import models
from datetime import datetime

class Imagem(models.Model):
    OPCOES_CATEGORIA = [
        ('PESSOA', 'pessoa'),
        ('CONSOLE', 'console'),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='imagem/%Y/%m/%d/', blank=True)
    eh_publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.nome
