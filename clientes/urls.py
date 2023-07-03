#from django.conf.urls improt url
from django.urls import path,include
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
    path('clientesReg', views.clientesReg, name='clientesReg'),
    path('clientes_del/<str:pk>', views.clientes_del, name='clientes_del'),  
    path('clientes_findEdit/<str:pk>', views.clientes_findEdit, name='clientes_findEdit'),
    path('clientesUpdate', views.clientesUpdate, name='clientesUpdate'),
    
    path("accounts/",include("django.contrib.auth.urls")),
]
