from django.shortcuts import render
from .models import Cliente,Genero
# Create your views here.
def index(request):
    clientes = Cliente.objects.all()
    context={"clientes":clientes}
    return render(request,'clientes/index.html',context)