import datetime
from django.shortcuts import render

# Create your views here.

def index(request):
    agora = datetime.datetime.now()
    return render(request, 'novoano/index.html', {
        'anonovo': agora.month == 1 and agora.day == 1
    })