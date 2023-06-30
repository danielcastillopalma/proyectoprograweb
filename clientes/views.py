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
def clientes_del(request,pk):
    try:
        cliente=Cliente.objects.get(rut=pk)
        
        cliente.delete()
        mensaje="Registro Eliminado"
        clientes=Cliente.objects.all()
        context = {'clientes':clientes, 'mensaje':mensaje}
        return render(request,'clientes/clientes_list.html',context)
    except:
        mensaje="Error, rut no existe"
        clientes=Cliente.objects.all()
        context = {'clientes':clientes, 'mensaje':mensaje}
        return render(request,'clientes/clientes_list.html',context)
        
def clientes_findEdit(request, pk):
    if pk!="":
        cliente=Cliente.objects.get(rut=pk)
        generos=Genero.objects.all()
        print(type(cliente.id_genero.genero))
        context={'cliente':cliente,'generos':generos}
        if cliente:
            return render(request,'clientes/clientes_edit.html',context)
        else:
            context={'error'}
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
        clientes=Cliente.objects.all()
        context={'clientes':clientes}
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

def clientesUpdate(request):
    if request.method=="POST":
        rut=request.POST["run"]
        nombre=request.POST["nombre"]
        apaterno=request.POST["apaterno"]
        amaterno=request.POST["apmaterno"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        activo="1"

        objGenero=Genero.objects.get(id_genero=genero)
        cliente=Cliente()
        cliente.rut              =rut,
        cliente.nombre           =nombre,
        cliente.apellido_paterno =apaterno,
        cliente.apellido_materno =amaterno,
        cliente.fecha_nacimiento ="1998-01-01",
        cliente.id_genero        =objGenero,
        cliente.telefono         =telefono,
        cliente.email            =email,
        cliente.direccion        =direccion,
        cliente.activo           =1
        cliente.save()
        
        generos=Genero.objects.all()
        context={'mensaje':"Datos actualizados",'generos':generos,'cliente':cliente}
        return render(request,'clientes/clientes_edit.html',context)
    else:
        clientes=Cliente.objects.all()
        context={'clientes':clientes}
        return render(request,'clientes/clientes_list.html',context)
