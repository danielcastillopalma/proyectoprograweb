from django.shortcuts import render
from .models import Cliente,Genero
# Create your views here.
def index(request):
    clientes = Cliente.objects.all()
    context={"clientes":clientes}
    return render(request,'clientes/index.html',context)
def login(request):
    context={}
    return render(request,'clientes/login.html',context)
def customizacion(request):
    context={}
    return render(request,'clientes/customizacion.html',context)
def repuestos(request):
    clientes = Cliente.objects.all()
    context={}
    return render(request,'clientes/repuestos.html',context)
def servicios(request):
    context={}
    return render(request,'clientes/servicios.html',context)