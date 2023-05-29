from django.db import models

# Create your models here.

class Producto(models.Model):
    id_producto = models.AutoField(db_column='idProducto',primary_key=True)
    nom_producto = models.CharField(max_length=20,blank=False,null=false)