from django.db import models

# Create your models here.
class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero = models.CharField(max_length=20,blank=False,null=False)
    def __str__(self):
        return str(self.genero)

class Cliente(models.Model):
    rut              = models.CharField( unique=True, max_length=10,blank=False,null=False)
    nombre           = models.CharField(max_length=20)
    password         = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=True, null=True) 
    id_genero        = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero' ,default=3)   
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(primary_key=True, max_length=100)
    direccion        = models.CharField(max_length=50, blank=True, null=True)  
    activo           = models.IntegerField()

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)   

class CategoriaProd(models.Model):
    id_categoria= models.AutoField(db_column='idCatProd',primary_key=True)
    categoria = models.CharField(max_length=50,blank=False,null=False)
    def __str__(self):
        return str(self.categoria)

class Producto(models.Model):
    id_producto=models.AutoField(db_column='idProd',primary_key=True)
    ##en la base de datos se modificará de forma artificial a un valor inicial de 10000+(n-1)
    nombre_producto=models.CharField(max_length=200,null=False,blank=False)
    marca_producto=models.CharField(max_length=200,null=False,blank=False)
    upc_producto=models.BigIntegerField(default=0)
    cantidad_paquete=models.CharField(default=0,max_length=50)
    valor_compra=models.IntegerField(default=0)
    valor_venta=models.IntegerField(default=0)
    

    