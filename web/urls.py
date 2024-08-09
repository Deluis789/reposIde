from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('registrar/', views.registrar, name='registrar'),
    path('crearUsuario/', views.crearUsuario, name='crearUsuario'), 
]