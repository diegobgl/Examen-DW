from django.urls import path

from .views import home, registro, perfil, suscripcion


urlpatterns = [
    path('',home, name ="home"),
    path('',perfil, name ="perfil"),
    path('',registro, name ="registro"),
    path('',suscripcion, name ="suscripcion"),
]
