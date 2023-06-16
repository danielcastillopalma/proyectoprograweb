#from django.conf.urls improt url
from django.urls import path
from . import views



urlpatterns =[
    path('index.html',views.index,name='index'),
    path('customizacion.html',views.customizacion,name='customizacion'),
    path('login.html',views.login,name='login'), 
    path('repuestos.html',views.repuestos,name='repuestos'),
    path('servicios.html',views.servicios,name='servicios')
]