from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Producto
from core.models import Usuario
from core.models import suscriptor
from core.models import detalle_venta
from core.models import venta 

from .serializers import ProductoSerializer, UsuarioSerializer 


#metodos usuarios
@csrf_exempt
@api_view(['GET'])
def listar_usuario(request):
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def agregarUsuario(request):
    usuario = Usuario.objects.create(
      
        nombre=request.POST['nombre'],
        password=request.POST['password'],
    )
    usuario.save()
    return Response([{"mensaje": "Se agrego correctamente"}])

@csrf_exempt
@api_view(['PUT'])
def editarUsuario(request, p_id):
    try:
        usuario = Usuario.objects.get(id=p_id)

        usuario.nombre = request.POST['nombre']
        usuario.password = request.POST['password']

        usuario.save()

        return Response([{"mensaje":"se Modifico correctamente"}])
    except Usuario.DoesNotExist:
        return Response(Usuario.errors, status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt
@api_view(['DELETE'])
def eliminarUsuario(request, p_id):
    try:
        usuario = Usuario.objects.get(id=p_id)
        
        usuario.delete()
        return Response([{"mensaje": "Se Elimino Correctamente"}])
        
    except Usuario.DoesNotExist:
        return Response(Usuario.errors, status=status.HTTP_400_BAD_REQUEST)

#metodos productos
@csrf_exempt
@api_view(['GET'])
def listar_producto(request):
    producto = Producto.objects.all()
    serializer = ProductoSerializer(producto, many=True)
    return Response(serializer.data)




@csrf_exempt
@api_view(['POST'])
def agregarProducto(request):

    producto = Producto.objects.create(
        nombre=request.POST['nombre'],
        descripcion=request.POST['descripcion'],
        valor=request.POST['valor']
    )
    producto.save()
    return Response([{"mensaje": "Se agrego correctamente el producto"}])


