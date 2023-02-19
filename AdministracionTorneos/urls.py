"""AdministracionTorneos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from APPadministracion.views import *
#
# Para el restfull
#
#from rest_framework import routers
from APPadministracion import views

"""
router = routers.DefaultRouter()
router.register(r'equipoRes', views.EquipoViewSet)
router.register(r'torneoRes', views.TorneoViewSet)
router.register(r'arbitroRes', views.ArbitroViewSet)
router.register(r'jugadorRes', views.JugadorViewSet)
router.register(r'implementoRes', views.ImplementoViewSet)
router.register(r'ticketRes', views.TicketViewSet)
router.register(r'encuentroRes', views.EncuentroViewSet)
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    #falta la ruta de principio
    path('',index),
    path('index/',index),
    #url para administrar (se accede a esta)
    path('administrador/',administrador),
    #Rutas de listado o rutas principales de cada clase
    path('jugadores/', listadoJugadores),
    path('equipos/', listadoEquipos),
    path('implementos/', listadoImplemento),
    path('ticket/', listadoTicket),
    path('arbitro/', listadoArbitros),
    path('torneo/', listadoTorneo),
    path('encuentro/', listadoEncuentro),
    #perfil
    path('perfil/',perfil),

    #rutas de api
    #path('api/', include(router.urls)),

    # Rutas de agregacion iniciales
    path('agregarPersona/', agregarPersona),
    path('agregarJugador/', agregarJugador),
    path('agregarEquipo/', agregarEquipo),
    path('agregarImplementos/', agregarImplementos),
    path('agregarTicket/', agregarTicket),
    path('agregarArbitro/', agregarArbitro),
    path('agregarTorneo/', agregarTorneo),
    path('agregarEncuentro/', agregarEncuentros),
    #rutas de busqueda importantes
    path('buscarTorneo/', buscarT),
    path('buscarEquipo/', buscarE),
    path('buscarJugador/', buscarJ),
    path('buscarArbitro/', buscarA),
    path('buscarImplemento/', buscarImple),
    path('buscarReserva/', buscarTic),
    path('buscarEncuentro/', buscarEncuentro),
    #rutas de eliminacion importantes
    path('eliminarPersona/<int:id>', eliminarPersona),
    path('eliminarArbitro/<int:id>', eliminarArbitro),
    path('eliminarJugador/<int:id>', eliminarJugador),
    path('eliminarEquipo/<int:id>', eliminarEquipo),
    path('eliminarImplemento/<int:id>', eliminarImplemento),
    path('eliminarTicket/<int:id>', eliminarTicket),
    path('eliminarTorneo/<int:id>', eliminarTorneo),
    path('eliminarEncuentro/<int:id>', eliminarEncuentro),
    #rutas de edicion importantes
    path('editarPersona/<int:id>', modificarPersona),
    path('editarArbitro/<int:id>', modificarArbitro),
    path('editarJugador/<int:id>', modificarJugador),
    path('editarEquipo/<int:id>', modificarEquipo),
    path('editarImplemento/<int:id>', modificarImplemento),
    path('editarTicket/<int:id>', modificarTicket),
    path('editarTorneo/<int:id>', modificarTorneo),
    path('editarEncuentro/<int:id>', modificarEncuentro),
    #Alternas de visualizacion
    path('masTorneo/<int:id>', mastorneo),
    path('verEquipo/<int:id>', verEquipo),
    path('verJugador/<int:id>', verJugador),
    path('verArbitro/<int:id>', verArbitro),
    path('verImplemento/<int:id>', verImplemento),
    path('verReserva/<int:id>', verReserva),
    path('verEncuentro/<int:id>', verEncuentro),
    #login 
    path('loginAdmin/', loginAdmin),
    #validacion
    path('validacion/', validar),
    #galeria
    path('galeria/', galeria),


]
