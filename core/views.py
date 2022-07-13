from django.shortcuts import  redirect, render

# Create your views here.

def  home (request):
    return render (request ,'core/home.html')

def  perfil (request):
    return render (request ,'core/perfil.html')

def registro(request):
    return render (request ,'core/registro.html') 

def suscripcion(request):
    return render (request ,'core/suscripcion.html')