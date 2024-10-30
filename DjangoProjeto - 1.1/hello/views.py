from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'hello/index.html')

def harry(request):
    return HttpResponse('Hello Harry')
'''
def name(request, name):
    return HttpResponse(f'Hello {name.capitalize()}')
'''
def name(request,name):
    return render(request, 'hello/greet.html', {'name': name.capitalize()})


