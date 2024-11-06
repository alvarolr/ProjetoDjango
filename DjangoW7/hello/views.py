from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'hello/index.html')

def harry(response):
    return HttpResponse('Ola Harry')

def rony(response):
    return HttpResponse('Ola Rony')

def hermione(response):
    return HttpResponse('Ola Hermione')

def saudacao(request, name):
    return render(request, 'hello/saudacao.html', {'name': name})