from django.urls import path

from .views import home, registro, perfil


urlpatterns = [
    path('',home, name ="home"),
    path('',perfil, name ="perfil"),
    path('',registro, name ="registro")
]
