from django.shortcuts import render
from .models import *
from datetime import datetime
from functools import wraps
import django.views.static
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    request.session["usuario"] = request.user.username
    usuario = request.session["usuario"]
    context = {'usuario': usuario}
    return render(request, 'clientes/index.html', context)


def login(request):
    context = {}
    return render(request, 'clientes/login.html', context)


def customizacion(request):
    context = {}
    return render(request, 'clientes/customizacion.html', context)


def repuestos(request):
    clientes = Cliente.objects.all()
    productos=Producto.objects.all()
    context = {'productos':productos}
    return render(request, 'clientes/repuestos.html', context)


def servicios(request):
    context = {}
    return render(request, 'clientes/servicios.html', context)


def register(request):
    generos = Genero.objects.all()
    context = {'generos': generos}
    return render(request, 'clientes/register.html', context)


def loginForm(request):
    context = {}
    return render(request, 'clientes/servicios.html', context)


def admin_check(user):
    if user.username == "admin":
        return True
    else:
        return False


@login_required
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
        context = {'generos': generos}
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
        objUser = User.objects.create_user(
            password=password,
            is_superuser="0",
            username=email,
            last_name=apaterno,
            email=email,
            is_staff="0",
            is_active="1",
            date_joined=datetime.now(),
            first_name=nombre
        )
        obj.save()
        context = {'mensaje': "Ok, datos grabados"}
        return render(request, ('registration/login.html'), context)


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


@login_required
def crud_prod(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'clientes/productos_list.html', context)


def productos_del(request, pk):
    try:
        producto = Producto.objects.get(id_producto=pk)

        producto.delete()
        mensaje = "Registro Eliminado"
        productos = Producto.objects.all()
        context = {'productos': productos, 'mensaje': mensaje}
        return render(request, 'clientes/productos_list.html', context)
    except:
        mensaje = "Error, rut no existe"
        productos = Producto.objects.all()
        context = {'productos': productos, 'mensaje': mensaje}
        return render(request, 'clientes/productos_list.html', context)


def productos_findEdit(request, pk):
    if pk != "":
        producto = Producto.objects.get(id_producto=pk)
        context = {'producto': producto}
        if producto:
            return render(request, 'clientes/productos_edit.html', context)
        else:
            context = {'error'}
            return render(request, 'clientes/clientes_list.html', context)


def productosAdd(request):
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


def productosUpdate(request):
    if request.method == "POST":
        id_prod= request.POST["id_prod"]
        nombre_prod = request.POST["nombre_prod"]
        marca = request.POST["marca"]
        upc = request.POST["upc"]
        cant_paquete = request.POST["cant_paquete"]
        valor_compra = request.POST["valor_compra"]
        valor_venta = request.POST["valor_venta"]
        stock = request.POST["stock"]
        img_prod = request.FILES.get("img_prod")


        pk = Producto.objects.get(id_producto=id_prod)
        producto = Producto()
        producto.id_producto = pk.id_producto
        producto.nombre_producto = nombre_prod
        producto.marca_producto = marca
        producto.upc_producto = upc
        producto.cantidad_paquete = cant_paquete
        producto.valor_compra = valor_compra
        producto.valor_venta = valor_venta
        producto.stock = stock
        producto.img_prod = img_prod
        producto.save()
        productos = Producto.objects.all()
        context = {'mensaje': "Datos actualizados",
                    'productos': productos}
        return render(request, 'clientes/productos_list.html', context)
    else:
        productos = Producto.objects.all()
        context = {'productos': productos}
        return render(request, 'clientes/productos_list.html', context)


def no_cache_static(f):
    @wraps(f)
    def static(*a, **kw):
        response = f(*a, **kw)
        response.headers["Cache-Control"] = "no-cache"
        return response

    return static


django.views.static.serve = no_cache_static(django.views.static.serve)
