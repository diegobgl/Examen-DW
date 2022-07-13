from pyexpat import model
from django.db import models
from django.forms import PasswordInput

# Create your models here.



#serializer ok,view serializer ok, 
class Producto(models.Model):
    id = models.AutoField(primary_key=True ,  unique=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    valor_p = models.IntegerField()


class Usuario(models.Model):
    id =models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=10)
    password = models.CharField(max_length=30)



class suscriptor(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField( max_length=50)
    fono = models.IntegerField()
    direccion = models.CharField(max_length=50)


class detalle_venta (models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    productos = models.CharField(max_length=50)
    total = models.IntegerField()





class venta(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    fecha = models.DateTimeField(auto_created=True)
    detalle_ventas =models.CharField(max_length=50)
    total_venta = models.IntegerField()
    descuento = models.IntegerField()
    iva =models.IntegerField()
    total = models.IntegerField()



    
# class registro(models.Model):
#     id = 
    