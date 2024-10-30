from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('harry', views.harry, name='harry'),
    path('<str:name>', views.name, name='name')
    
]
