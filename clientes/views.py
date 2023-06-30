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
def register(request):
    context={}
    return render(request,'clientes/register.html',context)
def crud(request):
    clientes=Cliente.objects.all()
    context={'clientes':clientes}
    return render(request,'clientes/clientes_list.html',context)

def clientesAdd(request):
    if request.method != "POST":
        generos=Genero.objects.all()
        context={'generos':generos}
        context={'mensaje': "Ok, datos no grabados"}
        return render(request,'clientes/clientes_add.html',context)

    else:
        rut=request.POST["run"]
        nombre=request.POST["nombre"]
        apaterno=request.POST["apaterno"]
        amaterno=request.POST["apmaterno"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        password=request.POST["password"]
        activo="1"

        objGenero=Genero.objects.get(id_genero=genero)
        obj=Cliente.objects.create(
        rut              =rut,
        nombre           =nombre,
        password         =password,
        apellido_paterno =apaterno,
        apellido_materno =amaterno,
        fecha_nacimiento ="1998-01-01",
        id_genero        =objGenero,
        telefono         =telefono,
        email            =email,
        direccion        =direccion,
        activo           =1)
        obj.save()
        context={'mensaje': "Ok, datos grabados"}
        return render(request,'clientes/clientes_list.html',context)
    
def clientesReg(request):
    if request.method != "POST":
        generos=Genero.objects.all()
        context={'generos':generos}
        context={'mensaje': "Ok, datos no grabados"}
        return render(request,'clientes/register.html',context)

    else:
        rut=request.POST["run"]
        nombre=request.POST["nombre"]
        apaterno=request.POST["apaterno"]
        amaterno=request.POST["apmaterno"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        password=request.POST["password"]
        activo="1"

        objGenero=Genero.objects.get(id_genero=genero)
        obj=Cliente.objects.create(
        rut              =rut,
        nombre           =nombre,
        password         =password,
        apellido_paterno =apaterno,
        apellido_materno =amaterno,
        fecha_nacimiento ="1998-01-01",
        id_genero        =objGenero,
        telefono         =telefono,
        email            =email,
        direccion        =direccion,
        activo           =1)
        obj.save()
        context={'mensaje': "Ok, datos grabados"}
        return render(request,'clientes/login.html',context)