from django.urls import path
from usuario.views import logout, view_login, view_cadastro

app_name = 'usuario'

urlpatterns = [
    path('login/', view_login, name='login'),
    path('cadastro/', view_cadastro, name='cadastro'),
    path('logout/', logout, name='logout'),
]


