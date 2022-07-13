from django.urls import path
from api_rest.views import  listar_usuario, agregarUsuario, editarUsuario, eliminarUsuario

urlpatterns = [
    
    path('listar_usuario/',listar_usuario, name="listar_usuario"),
    path('agregar_usuario/',agregarUsuario ),
    path('editarUsuario/<p_id>',editarUsuario),
    path('eliminarUsuario/<p_id>',eliminarUsuario)
]
