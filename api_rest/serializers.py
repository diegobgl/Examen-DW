from dataclasses import fields
from rest_framework import serializers
from core.models import Usuario, Producto, suscriptor, venta, detalle_venta


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','nombre', 'password']
        #fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'valor_p' ]

class SuscriptorSerializer (serializers.ModelSerializer):
    class Meta:
        model = suscriptor 
        fields = ['id','nombre_s','apellido_s','correo_s','fono','direccion']

class venta(serializers.ModelSerializer):
    class meta:
        model = venta
        fields = ['id',' fecha','detalle_ventas','total_venta','descuento']

