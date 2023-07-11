from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)


class Cliente(models.Model):
    rut = models.CharField(unique=True, max_length=10, blank=False, null=False)
    nombre = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    id_genero = models.ForeignKey(
        'Genero', on_delete=models.CASCADE, db_column='idGenero', default=3)
    telefono = models.CharField(max_length=45)
    email = models.EmailField(primary_key=True, max_length=100)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.IntegerField()

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)


class SubCategoriaProd(models.Model):
    id_categoria = models.AutoField(db_column='idCatProd', primary_key=True)
    categoria = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return str(self.categoria)


class CategoriaProd(models.Model):
    id_categoria = models.AutoField(db_column='idCatProd', primary_key=True)
    categoria = models.CharField(max_length=50, blank=False, null=False)
    id_subCat = models.ForeignKey(
        'SubCategoriaProd', on_delete=models.CASCADE, db_column='SubCategoriaProd.idCatProd')

    def __str__(self):
        return str(self.categoria)


class Producto(models.Model):
    id_producto = models.AutoField(db_column='idProd', primary_key=True)
    # en la base de datos se modificará de forma artificial a un valor inicial de 10000+(n-1)
    nombre_producto = models.CharField(max_length=200, null=False, blank=False)
    marca_producto = models.CharField(max_length=200, null=False, blank=False)
    upc_producto = models.BigIntegerField(default=0)
    cantidad_paquete = models.CharField(default=0, max_length=50)
    valor_compra = models.IntegerField(default=0)
    valor_venta = models.IntegerField(default=0)
    img_prod = models.ImageField(upload_to='productos', null=True)
    id_cat = models.ForeignKey(
        'CategoriaProd', on_delete=models.CASCADE, db_column='idCatProd', default=1)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return str(self.nombre_producto)


class Boleta(models.Model):
    num_boleta = models.AutoField(db_column="num_boleta", primary_key=True)
    fecha_boleta = models.DateField(blank=False, null=False)
    num_cliente = models.ForeignKey(
        'Cliente', on_delete=models.CASCADE, db_column='rut')
    monto_boleta = models.IntegerField(default=0, null=False)
    activa = models.IntegerField()


class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    @property
    def total_price(self):
        cartitems = self.cartitems.all()
        total = sum([item.price for item in cartitems])
        return total

    @property
    def num_of_items(self):
        cartitems = self.cartitems.all()
        quantity = sum([item.quantity for item in cartitems])
        return quantity


class CartItem(models.Model):
    product = models.ForeignKey(
        Producto, on_delete=models.CASCADE, related_name='items')
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="cartitems")
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product.nombre_producto

    @property
    def price(self):
        new_price = self.product.valor_venta * self.quantity
        return new_price
   
