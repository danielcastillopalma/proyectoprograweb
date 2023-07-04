#from django.conf.urls improt url
from django.urls import path,include
from . import views
urlpatterns =[
    path('menu',views.menu,name='menu'),
]