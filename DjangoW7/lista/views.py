from django.shortcuts import render, redirect

# Create your views here.

items = ['comprar maça', 'correr', 'estudar']

def index(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        if item_name:
            items.append(item_name)  # Adiciona o item à lista
        return redirect('index')
    return render(request, 'lista/index.html', {'items': items})