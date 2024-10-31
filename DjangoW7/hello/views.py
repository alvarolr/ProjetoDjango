from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse('Ola mundo')

def harry(response):
    return HttpResponse('Ola Harry')

def rony(response):
    return HttpResponse('Ola Rony')

def hermione(response):
    return HttpResponse('Ola Hermione')

def saudacao(response, name):
    return HttpResponse(f'Ola {name}')