# from django.conf.urls improt url
from django.urls import path, include
from . import views


urlpatterns = [
    path("cart", views.cart, name="cart"),
    path("add_to_cart", views.add_to_cart, name="add"),
    path("remove_from_cart", views.remove_from_cart, name="remove"),
    path("confirm_payment/<str:pk>", views.confirm_payment, name="confirm_payment"),
    
    path("search", views.search, name="search"),

    path('index', views.index, name='index'),
    path('customizacion', views.customizacion, name='customizacion'),
    path('login', views.login, name='login'),
    path('repuestos', views.repuestos, name='repuestos'),
    path('servicios', views.servicios, name='servicios'),
    path('register', views.register, name='register'),

    path('crud', views.crud, name='crud'),
    path('clientesAdd', views.clientesAdd, name='clientesAdd'),
    path('clientesReg', views.clientesReg, name='clientesReg'),
    path('clientes_del/<str:pk>', views.clientes_del, name='clientes_del'),
    path('clientes_findEdit/<str:pk>',
         views.clientes_findEdit, name='clientes_findEdit'),
    path('clientesUpdate', views.clientesUpdate, name='clientesUpdate'),


    path('crud_prod', views.crud_prod, name='crud_prod'),
    path('productosAdd', views.productosAdd, name='productosAdd'),
    path('productos_del/<str:pk>', views.productos_del, name='productos_del'),
    path('productos_findEdit/<str:pk>',
         views.productos_findEdit, name='productos_findEdit'),
    path('productosUpdate', views.productosUpdate, name='productosUpdate'),
]
