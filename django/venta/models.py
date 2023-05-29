elfrom django.db import models

# Create your models here.

class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero',primary_key=True)
    genero = models.CharField(max_length=20,blank=False,null=false)
    def__str__(self):
        return str(self.genero)
class Alumno(models.Model):
    rut = models.CharField(primary_key=True,max_length=10)
    nombre= models.CharField(max_length=20)
    apellido_paterno= models.CharField(max_length=20)
    apellido_materno= models.CharField(max_length=20)
    fecha_nacimiento=models.DateField(blank=False,null=False)
    id_genero=models.ForeignKey('Genero',on_delete=models.CASCADE,db_column='idGenero')
    telefono = models.CharField(max_length=45)
    email=models.EmailField(unique=True,max_lenght=100,blank=True,null=True)
    direccion=models.CharField(max_lenght=50,blank=True,null=True)
    activo=models.IntegerField()

    def__str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)