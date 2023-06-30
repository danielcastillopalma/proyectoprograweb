#from django.conf.urls improt url
from django.urls import path
from . import views



urlpatterns =[
    path('index',views.index,name='index'),
    path('customizacion',views.customizacion,name='customizacion'),
    path('login',views.login,name='login'), 
    path('repuestos',views.repuestos,name='repuestos'),
    path('servicios',views.servicios,name='servicios'),
    path('register',views.register, name='register'),
    path('crud', views.crud, name='crud'),
    path('clientesAdd', views.clientesAdd, name='clientesAdd'),
    
]
