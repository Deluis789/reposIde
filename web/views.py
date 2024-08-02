from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request, 'usuario/login.html', {})
def registrar(request):
    return render(request, 'usuario/formulario.html', {})