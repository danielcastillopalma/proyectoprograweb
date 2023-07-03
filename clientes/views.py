from django.shortcuts import render
from .models import Cliente, Genero
from datetime import datetime
from functools import wraps
import django.views.static

# Create your views here.


def index(request):
    clientes = Cliente.objects.all()
    context = {"clientes": clientes}
    return render(request, 'clientes/index.html', context)


def login(request):
    context = {}
    return render(request, 'clientes/login.html', context)


def customizacion(request):
    context = {}
    return render(request, 'clientes/customizacion.html', context)


def repuestos(request):
    clientes = Cliente.objects.all()
    context = {}
    return render(request, 'clientes/repuestos.html', context)



def servicios(request):
    context = {}
    return render(request, 'clientes/servicios.html', context)


def register(request):
    generos = Genero.objects.all()
    context = {'generos': generos}
    return render(request, 'clientes/register.html', context)


def crud(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, 'clientes/clientes_list.html', context)


def clientes_del(request, pk):
    try:
        cliente = Cliente.objects.get(rut=pk)

        cliente.delete()
        mensaje = "Registro Eliminado"
        clientes = Cliente.objects.all()
        context = {'clientes': clientes, 'mensaje': mensaje}
        return render(request, 'clientes/clientes_list.html', context)
    except:
        mensaje = "Error, rut no existe"
        clientes = Cliente.objects.all()
        context = {'clientes': clientes, 'mensaje': mensaje}
        return render(request, 'clientes/clientes_list.html', context)


def clientes_findEdit(request, pk):
    if pk != "":
        cliente = Cliente.objects.get(rut=pk)
        generos = Genero.objects.all()
        print(type(cliente.id_genero.genero))
        context = {'cliente': cliente, 'generos': generos}
        if cliente:
            return render(request, 'clientes/clientes_edit.html', context)
        else:
            context = {'error'}
            return render(request, 'clientes/clientes_list.html', context)


def clientesAdd(request):
    if request.method != "POST":
        generos = Genero.objects.all()
        context = {'generos': generos}
        return render(request, 'clientes/clientes_add.html', context)

    else:
        rut = request.POST["run"]
        nombre = request.POST["nombre"]
        apaterno = request.POST["apaterno"]
        amaterno = request.POST["apmaterno"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        fechanacimiento = request.POST["fecnac"]
        direccion = request.POST["direccion"]
        password = request.POST["password"]
        activo = "1"

        objGenero = Genero.objects.get(id_genero=genero)
        obj = Cliente.objects.create(
            rut=rut,
            nombre=nombre,
            password=password,
            apellido_paterno=apaterno,
            apellido_materno=amaterno,
            fecha_nacimiento=fechanacimiento,
            id_genero=objGenero,
            telefono=telefono,
            email=email,
            direccion=direccion,
            activo=1)
        obj.save()
        clientes = Cliente.objects.all()
        context = {'clientes': clientes}
        return render(request, 'clientes/clientes_list.html', context)


def clientesReg(request):
    if request.method != "POST":
        generos = Genero.objects.all()
        context = {'genero': generos}
        return render(request, 'clientes/register.html', context)

    else:
        rut = request.POST["run"]
        nombre = request.POST["nombre"]
        apaterno = request.POST["apaterno"]
        amaterno = request.POST["apmaterno"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        fechanacimiento = request.POST["fecnac"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        password = request.POST["password"]
        activo = "1"

        objGenero = Genero.objects.get(id_genero=genero)
        obj = Cliente.objects.create(
            rut=rut,
            nombre=nombre,
            password=password,
            apellido_paterno=apaterno,
            apellido_materno=amaterno,
            fecha_nacimiento=fechanacimiento,
            id_genero=objGenero,
            telefono=telefono,
            email=email,
            direccion=direccion,
            activo=1)
        obj.save()
        context = {'mensaje': "Ok, datos grabados"}
        return render(request, 'clientes/login.html', context)


def clientesUpdate(request):
    if request.method == "POST":
        rut = request.POST["run"]
        nombre = request.POST["nombre"]
        apaterno = request.POST["apaterno"]
        amaterno = request.POST["apmaterno"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = "1"

        pk = Cliente.objects.get(rut=rut)
        password = pk.password
        fecnac = pk.fecha_nacimiento
        objGenero = Genero.objects.get(id_genero=genero)

        cliente = Cliente()
        cliente.rut = rut
        cliente.nombre = nombre
        cliente.apellido_paterno = apaterno
        cliente.apellido_materno = amaterno
        cliente.telefono = telefono
        cliente.id_genero = objGenero
        cliente.password = password
        cliente.email = email
        cliente.fecha_nacimiento = fecnac
        cliente.direccion = direccion
        cliente.activo = 1
        cliente.save()
        generos = Genero.objects.all()
        clientes = Cliente.objects.all()
        context = {'mensaje': "Datos actualizados",
                   'generos': generos, 'clientes': clientes}
        return render(request, 'clientes/clientes_list.html', context)
    else:
        clientes = Cliente.objects.all()
        context = {'clientes': clientes}
        return render(request, 'clientes/clientes_list.html', context)


def no_cache_static(f):
    @wraps(f)
    def static(*a, **kw):
        response = f(*a, **kw)
        response.headers["Cache-Control"] = "no-cache"
        return response

    return static


django.views.static.serve = no_cache_static(django.views.static.serve)
