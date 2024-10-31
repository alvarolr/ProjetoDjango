from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('harry/', views.harry, name='harry'),
    path('rony/', views.rony, name='rony'),
    path('hermione/', views.hermione, name='hermione'),
    path('<str:name>/', views.saudacao, name='saudacao')
]
