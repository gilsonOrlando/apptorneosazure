from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from APPadministracion.models import Persona, Torneo, Arbitro, Ticket, Equipo, Jugador, Implementos, Encuentro
from APPadministracion.forms import FormularioArbitro, FormularioEquipo, FormularioImplementos, FormularioJugador, \
    FormularioPersona, FormularioTicket, FormularioTorneo, FormularioEncuentro
from django.contrib import messages

from django.core.exceptions import ValidationError  #


#
#
# Agregaciones nuevas 2022
#
#
#

def galeria(request):  # ventana para mostrar una simple galeria de fotografias
    return render(request, "galeria.html", {})


# Create your views here.
#
#
# vistas principales 
#
#
def index(request):  # pestaña para el usuario
    return render(request, "index.html", {})


def administrador(request):  # pestaña para operaciones  (Agregar/Eliminar....)
    return render(request, "administrador.html")


def contacto(request):
    return render(request, 'Contacto.html', {})


def informacion(request):
    return render(request, 'Informacion.html', {})


def loginAdmin(request):
    return render(request, 'loginAdmin.html', {})


#
#
# importaciones para el restfull
#
#
# from rest_framework import viewsets
from django.http import Http404

# from rest_framework import status
# from rest_framework.response import Response

# from APPadministracion.serializers import arbitroSerializer, encuentroSerializer, implementoSerializer, jugadorSerializer, ticketSerializer, torneoSerializer, equipoSerializer
# Create your views here.
#
#
# Serializables 
#
#
#
"""
class TorneoViewSet(viewsets.ModelViewSet):       
    queryset = Torneo.objects.all().order_by('id')
    serializer_class = torneoSerializer

class EquipoViewSet(viewsets.ModelViewSet):    
    
    queryset = Equipo.objects.all().order_by('id')
    serializer_class = equipoSerializer

class JugadorViewSet(viewsets.ModelViewSet):    
    
    queryset = Jugador.objects.all().order_by('id')
    serializer_class = jugadorSerializer

class ArbitroViewSet(viewsets.ModelViewSet):    
    
    queryset = Arbitro.objects.all().order_by('id')
    serializer_class = arbitroSerializer

class ImplementoViewSet(viewsets.ModelViewSet):    
    
    queryset = Implementos.objects.all().order_by('id')
    serializer_class = implementoSerializer

class TicketViewSet(viewsets.ModelViewSet):    
    
    queryset = Ticket.objects.all().order_by('id')
    serializer_class = ticketSerializer

class EncuentroViewSet(viewsets.ModelViewSet):    
    
    queryset = Encuentro.objects.all().order_by('id')
    serializer_class = encuentroSerializer
"""

#
#
# Vistas de agregados de cada una de las clases 
#
#

# implementaciones del form Persona
"""
class RegistrarPersonaView(generic.FormView):
    templeate_name = 'agregarPersona.html'
    form_class = FormularioPersona
    model = Persona
   
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
        
        """


def agregarPersona(request):
    if request.method == 'POST':
        formularioPersona = FormularioPersona(request.POST)
        if formularioPersona.is_valid():
            if formularioPersona.save() != True:
                print('Imprimo en pantalla y guardo los datos en la bd')
                print(formularioPersona.cleaned_data)
                messages.success(request, 'Se ha registrado correctamente')
                return redirect(to='/loginAdmin/')
            else:
                print('No se pudo guardar los datos')
                messages.error(request, 'No se pudo registrar')
                return redirect(to='/agregarPersona/')
    else:
        formularioPersona = FormularioPersona()
    return render(request, 'agregarPersona.html', {"formularioPersona": formularioPersona})


# implementaciones del form Torneo

def agregarTorneo(request):
    formularioTorneo = FormularioTorneo(request.GET or None)
    if request.method == 'GET':
        if formularioTorneo.is_valid():
            datosTorneo = formularioTorneo.cleaned_data
            torneo = Torneo()
            torneo.nombre = datosTorneo.get("nombre")
            torneo.alias = datosTorneo.get("alias")
            torneo.numeroEquipo = datosTorneo.get("numeroEquipo")
            torneo.descripcion = datosTorneo.get("descripcion")
            torneo.fechaInicio = datosTorneo.get("fechaInicio")
            torneo.fechaFin = datosTorneo.get("fechaFin")
            torneo.tipo_Tor = datosTorneo.get("tipo_Tor")
            if torneo.save() != True:
                print('Imprimo en pantalla y guardo los datos en la bd')
                print(formularioTorneo.cleaned_data)
                return redirect(to='/torneo/')
    return render(request, 'agregarTorneo.html', {"formularioTorneo": formularioTorneo})


# implementaciones del form Implementos
def agregarImplementos(request):
    formularioImplementos = FormularioImplementos(request.GET or None)
    if request.method == 'GET':
        if formularioImplementos.is_valid():
            datosImplemento = formularioImplementos.cleaned_data
            implemento = Implementos()
            implemento.PropiedadTorneo = datosImplemento.get("PropiedadTorneo")
            implemento.nombre = datosImplemento.get("nombre")
            implemento.cantidad = datosImplemento.get("cantidad")
            implemento.descripcion = datosImplemento.get("descripcion")
            implemento.tipo_Im = datosImplemento.get("tipo_Im")
            if implemento.save() != True:
                print('Imprimo en pantalla y guardo los datos en la bd')
                print(formularioImplementos.cleaned_data)
                return redirect(to='/implementos/')
    return render(request, 'agregarImplementosDeportivos.html', {"formularioImplementos": formularioImplementos})


# implementaciones del form Arbitro
def agregarArbitro(request):
    formularioArbitro = FormularioArbitro(request.GET or None)
    if request.method == 'GET':
        if formularioArbitro.is_valid():
            datosArbitro = formularioArbitro.cleaned_data
            arbitro = Arbitro()
            arbitro.PropiedadTorneo = datosArbitro.get("PropiedadTorneo")
            arbitro.nombre = datosArbitro.get("nombre")
            arbitro.apellido = datosArbitro.get("apellido")
            arbitro.correo = datosArbitro.get("correo")
            arbitro.celular = datosArbitro.get("celular")
            arbitro.cedula = datosArbitro.get("cedula")
            if arbitro.save() != True:
                print('Imprimo en pantalla y guardo los datos en la bd')
                print(formularioArbitro.cleaned_data)
                return redirect(to='/arbitro/')
    return render(request, 'agregarArbitros.html', {"formularioArbitro": formularioArbitro})


# implementaciones del form Ticket
def agregarTicket(request):
    formularioTicket = FormularioTicket(request.GET or None)
    if request.method == 'GET':
        if formularioTicket.is_valid():
            datostic = formularioTicket.cleaned_data
            tic = Ticket()
            tic.PropiedadTorneo = datostic.get("PropiedadTorneo")
            tic.nombre = datostic.get("nombre")
            tic.apellido = datostic.get("apellido")
            tic.correo = datostic.get("correo")
            tic.cedula = datostic.get("cedula")
            tic.estado_Ticket = datostic.get("estado_Ticket")
            if tic.save() != True:
                print('Imprimo en pantalla y guardo los datos en la bd')
                print(formularioTicket.cleaned_data)
                return redirect(to='/ticket/')
    return render(request, 'agregarReserva.html', {"formularioTicket": formularioTicket})


# implementaciones del form Equipo
def agregarEquipo(request):
    formularioEquipo = FormularioEquipo(request.GET or None)
    if request.method == 'GET':
        if formularioEquipo.is_valid():
            datosEquipo = formularioEquipo.cleaned_data
            equipo = Equipo()
            equipo.PropiedadTorneo = datosEquipo.get("PropiedadTorneo")
            equipo.nombre = datosEquipo.get("nombre")
            equipo.alias = datosEquipo.get("alias")
            equipo.frase = datosEquipo.get("frase")
            equipo.entrenador = datosEquipo.get("entrenador")
            equipo.cantidadJugador = datosEquipo.get("cantidadJugador")
            equipo.estado_Equipo = datosEquipo.get("estado_Equipo")
            if equipo.save() != True:
                print('Imprimo en pantalla y guardo los datos en la bd')
                print(formularioEquipo.cleaned_data)
                return redirect(to='/equipos/')
    return render(request, 'agregarEquipos.html', {"formularioEquipo": formularioEquipo})


# implementaciones del form Jugador
def agregarJugador(request):
    formularioJugador = FormularioJugador(request.GET or None)
    if request.method == 'GET':
        if formularioJugador.is_valid():
            datosJugador = formularioJugador.cleaned_data
            jugador = Jugador()
            jugador.PropiedadEquipo = datosJugador.get("PropiedadEquipo")
            jugador.nombre = datosJugador.get("nombre")
            jugador.apellido = datosJugador.get("apellido")
            jugador.correo = datosJugador.get("correo")
            jugador.celular = datosJugador.get("celular")
            jugador.cedula = datosJugador.get("cedula")
            jugador.posicion_Jugador = datosJugador.get("posicion_Jugador")
            if jugador.save() != True:
                print('Imprimo en pantalla y guardo los datos en la bd')
                print(formularioJugador.cleaned_data)
                return redirect(to='/jugadores/')
    return render(request, 'agregarJugadores.html', {"formularioJugador": formularioJugador})


# implementaciones del form Encuentro
def agregarEncuentros(request):
    formularioEncuentro = FormularioEncuentro(request.GET or None)
    # tor = Torneo.objects.filter(id__icontains=id)
    if request.method == 'GET':
        if formularioEncuentro.is_valid():
            datosEncuentro = formularioEncuentro.cleaned_data
            encuentro = Encuentro()
            encuentro.PropiedadTorneo = datosEncuentro.get("PropiedadTorneo")
            encuentro.nombreA = datosEncuentro.get("nombreA")
            encuentro.nombreB = datosEncuentro.get("nombreB")
            encuentro.fechaPartido = datosEncuentro.get("fechaPartido")
            encuentro.hora = datosEncuentro.get("hora")
            encuentro.golesA = datosEncuentro.get("golesA")
            encuentro.golesB = datosEncuentro.get("golesB")
            encuentro.faltas = datosEncuentro.get("faltas")
            encuentro.tarjetaRoja = datosEncuentro.get("tarjetaRoja")
            encuentro.tarjetaAmarilla = datosEncuentro.get("tarjetaAmarilla")
            if encuentro.save() != True:
                print('Imprimo en pantalla y guardo los datos en la bd')
                print(formularioEncuentro.cleaned_data)
                return redirect(to='/encuentro/')
    # return render(request,'agregarEncuentros.html',{"formularioEncuentro":formularioEncuentro,"torneo":tor})
    return render(request, 'agregarEncuentros.html', {"formularioEncuentro": formularioEncuentro})


#
#
# Vistas de busqueda de cada una de las clases 
#
#

# busqueda de arbitro
def buscarA(request):
    # controlamos que no se envie una peticion de busqueda vacia
    if request.GET["textobuscar"]:
        arbitro = request.GET["textobuscar"]
        if len(arbitro) < 30:
            arbi = Arbitro.objects.filter(nombre__icontains=arbitro)
            if arbi:
                return render(request, "busquedaArbitro.html", {"arbitro": arbi})
            else:
                return redirect(to='/arbitro/')
        else:
            return redirect(to='/arbitro/')
    else:
        return redirect(to='/arbitro/')


# busqueda de jugador
def buscarJ(request):
    # controlamos que no se envie una peticion de busqueda vacia
    if request.GET["textobuscar"]:
        jugador = request.GET["textobuscar"]
        if len(jugador) < 30:
            juga = Jugador.objects.filter(nombre__icontains=jugador)
            if juga:
                return render(request, "busquedaJugador.html", {"jugador": juga})
            else:
                return redirect(to='/jugadores/')
        else:
            return redirect(to='/jugadores/')
    else:
        return redirect(to='/jugadores/')


# busqueda de ticket
def buscarTic(request):
    # controlamos que no se envie una peticion de busqueda vacia
    if request.GET["textobuscar"]:
        ticket = request.GET["textobuscar"]
        if len(ticket) < 30:
            tick = Ticket.objects.filter(nombre__icontains=ticket)
            if tick:
                return render(request, "busquedaTicket.html", {"ticket": tick})
            else:
                return redirect(to='/ticket/')
        else:
            return redirect(to='/ticket/')
    else:
        return redirect(to='/ticket/')


def buscarE(request):
    # controlamos que no se envie una peticion de busqueda vacia
    if request.GET["textobuscar"]:
        equipo = request.GET["textobuscar"]
        if len(equipo) < 30:
            equi = Equipo.objects.filter(nombre__icontains=equipo)
            if equi:
                return render(request, "busquedaEquipo.html", {"equipo": equi})
            else:
                return redirect(to='/equipos/')
        else:
            return redirect(to='/equipos/')
    else:
        return redirect(to='/equipos/')


def buscarT(request):
    # controlamos que no se envie una peticion de busqueda vacia
    if request.GET["textobuscar"]:
        torneo = request.GET["textobuscar"]
        if len(torneo) < 30:
            tor = Torneo.objects.filter(nombre__icontains=torneo)
            if tor:
                return render(request, "busquedaTorneo.html", {"torneo": tor})
            else:
                return redirect(to='/torneo/')
        else:
            return redirect(to='/torneo/')
    else:
        return redirect(to='/torneo/')


# busqueda de implementos
def buscarImple(request):
    # controlamos que no se envie una peticion de busqueda vacia
    if request.GET["textobuscar"]:
        implemento = request.GET["textobuscar"]
        if len(implemento) < 30:
            imple = Implementos.objects.filter(nombre__icontains=implemento)
            if imple:
                return render(request, "busquedaImplemento.html", {"implemento": imple})
            else:
                return redirect(to='/implementos/')
        else:
            return redirect(to='/implementos/')
    else:
        return redirect(to='/implementos/')


# busqueda de encuentros
def buscarEncuentro(request):
    # controlamos que no se envie una peticion de busqueda vacia
    if request.GET["textobuscar"]:
        encuentro = request.GET["textobuscar"]
        if len(encuentro) < 30:
            encu = Encuentro.objects.filter(nombreA__icontains=encuentro)
            if encu:
                return render(request, "busquedaEncuentro.html", {"encuentro": encu})
            else:
                return redirect(to='/encuentro/')
        else:
            return redirect(to='/encuentro/')
    else:
        return redirect(to='/encuentro/')


#
#
# Vistas de listado de cada una de las clases 
#
#
#

def listadoArbitros(request):  # listar arbitros
    listaArbitro = Arbitro.objects.all()
    return render(request, 'misArbitros.html', {"listaArbitro": listaArbitro})


def listadoJugadores(request):  # listar jugadores
    listaJugador = Jugador.objects.all()
    return render(request, 'misJugadores.html', {"listaJugador": listaJugador})


def listadoTicket(request):  # listar tickets
    listaTicket = Ticket.objects.all()
    return render(request, 'misReservas.html', {"listaTicket": listaTicket})


def listadoTorneo(request):  # listar torneo
    listaTorneo = Torneo.objects.all()
    return render(request, 'mistorneos.html', {"listaTorneo": listaTorneo})


def listadoEquipos(request):  # listar equipos
    listaEquipo = Equipo.objects.all()
    return render(request, 'misEquipos.html', {"listaEquipo": listaEquipo})


def listadoImplemento(request):  # listar implemento
    listaImplemento = Implementos.objects.all()
    return render(request, 'misImplementosDeportivos.html', {"listaImplemento": listaImplemento})


def listadoEncuentro(request):  # listar encuentros (modificar)
    listaEncuentro = Encuentro.objects.all()
    # tor = Torneo.objects.filter(id__icontains=id)
    # return render(request, 'misEncuentros.html',{"listaEncuentro":listaEncuentro, 'torneo':tor} )
    return render(request, 'misEncuentros.html', {"listaEncuentro": listaEncuentro})


#
#
# Vistas de eliminacion de cada una de las clases 
#
#
#

# ARREGLAR LAS REDIRECCIONES
# las redirecciones son a las propias paginas principales de cada seccion
def eliminarArbitro(request, id):
    arbitro = Arbitro.objects.get(id=id)
    arbitro.delete()
    print('Se borro')
    # se redirige la pagina
    return redirect('/arbitro/')


def eliminarJugador(request, id):
    jugador = Jugador.objects.get(id=id)
    jugador.delete()
    print('Se borro')
    # se redirige la pagina
    return redirect('/jugadores/')


def eliminarPersona(request, id):
    persona = Persona.objects.get(id=id)
    persona.delete()
    print('Se borro')
    # se redirige la pagina
    return redirect('/loginAdmin/')


def eliminarTicket(request, id):
    tic = Ticket.objects.get(id=id)
    tic.delete()
    print('Se borro')
    # se redirige la pagina
    return redirect('/ticket/')


def eliminarTorneo(request, id):
    torneo = Torneo.objects.get(id=id)
    torneo.delete()
    print('Se borro')
    # se redirige la pagina
    return redirect('/torneo/')


def eliminarEquipo(request, id):
    equipo = Equipo.objects.get(id=id)
    equipo.delete()
    print('Se borro')
    # se redirige la pagina
    return redirect('/equipos/')


def eliminarImplemento(request, id):
    imple = Implementos.objects.get(id=id)
    imple.delete()
    print('Se borro')
    # se redirige la pagina
    return redirect('/implementos/')


def eliminarEncuentro(request, id):
    listaEncuentro = Encuentro.objects.all()
    encuentro = Encuentro.objects.get(id=id)
    # idTor = encuentro.get("PropiedadTorneo")
    # tor = Torneo.objects.get(id=encuentro.get("PropiedadTorneo"))
    print('||||')
    print('||||')
    print('||||')
    print('||||')
    # print(encuentro.get("nombreA"))
    print('||||')
    print('||||')
    print('||||')
    print('||||')
    print('*******')
    encuentro.delete()
    print('Se borro')
    # se redirige la pagina
    # return render(request, 'misEncuentros.html',{"listaEncuentro":listaEncuentro, 'torneo':tor} )
    return redirect('/torneo/')
    # return redirect('/encuentro/')


#
#
# Actualizacion
#
#
def modificarPersona(request, id):  # modificacion del admin
    # busca en el modelo correspondiente para poder modificar la informacion
    persona = get_object_or_404(Persona, id=id)
    data = {
        'form': FormularioPersona(instance=persona)
    }
    if request.method == 'GET':
        formulario = FormularioPersona(data=request.GET, instance=persona)
        if formulario.is_valid():
            formulario.save()
            print('Se actualizo')
            return redirect(to='/home/')
        data["form"] = formulario
    return render(request, 'editarPersona.html', data)


def modificarArbitro(request, id):  # modificacion del arbitro
    # busca en el modelo correspondiente para poder modificar la informacion
    arbitro = get_object_or_404(Arbitro, id=id)
    data = {
        'form': FormularioArbitro(instance=arbitro)
    }
    if request.method == 'GET':
        formulario = FormularioArbitro(data=request.GET, instance=arbitro)
        if formulario.is_valid():
            formulario.save()
            print('Se actualizo')
            return redirect(to='/arbitro/')
        data["form"] = formulario
    return render(request, 'editarArbitros.html', data)


def modificarJugador(request, id):  # modificacion del jugador
    # busca en el modelo correspondiente para poder modificar la informacion
    jugador = get_object_or_404(Jugador, id=id)
    data = {
        'form': FormularioJugador(instance=jugador)
    }
    if request.method == 'GET':
        formulario = FormularioJugador(data=request.GET, instance=jugador)
        if formulario.is_valid():
            formulario.save()
            print('Se actualizo')
            return redirect(to='/jugadores/')
        data["form"] = formulario
    return render(request, 'editarJugadores.html', data)


def modificarTicket(request, id):  # modificacion del ticket
    # busca en el modelo correspondiente para poder modificar la informacion
    ticket = get_object_or_404(Ticket, id=id)
    data = {
        'form': FormularioTicket(instance=ticket)
    }
    if request.method == 'GET':
        formulario = FormularioTicket(data=request.GET, instance=ticket)
        if formulario.is_valid():
            formulario.save()
            print('Se actualizo')
            return redirect(to='/misReservas/')
        data["form"] = formulario
    return render(request, 'editarReserva.html', data)


def modificarTorneo(request, id):  # modificacion del torneo
    # busca en el modelo correspondiente para poder modificar la informacion
    torneo = get_object_or_404(Torneo, id=id)
    data = {
        'form': FormularioTorneo(instance=torneo)
    }
    if request.method == 'GET':
        formulario = FormularioTorneo(data=request.GET, instance=torneo)
        if formulario.is_valid():
            formulario.save()
            print('Se actualizo')
            return redirect(to='/torneo/')
        data["form"] = formulario
    return render(request, 'editarTorneo.html', data)


def modificarEquipo(request, id):  # modificacion del equipo
    # busca en el modelo correspondiente para poder modificar la informacion
    equipo = get_object_or_404(Equipo, id=id)
    data = {
        'form': FormularioEquipo(instance=equipo)
    }
    if request.method == 'GET':
        formulario = FormularioEquipo(data=request.GET, instance=equipo)
        if formulario.is_valid():
            formulario.save()
            print('Se actualizo')
            return redirect(to='/equipos/')
        data["form"] = formulario
    return render(request, 'editarEquipos.html', data)


def modificarImplemento(request, id):  # modificacion del implemento
    # busca en el modelo correspondiente para poder modificar la informacion
    implemento = get_object_or_404(Implementos, id=id)
    data = {
        'form': FormularioImplementos(instance=implemento)
    }
    if request.method == 'GET':
        formulario = FormularioImplementos(data=request.GET, instance=implemento)
        if formulario.is_valid():
            formulario.save()
            print('Se actualizo')
            return redirect(to='/implementos/')
        data["form"] = formulario
    return render(request, 'editarImplementosDeportivos.html', data)


def modificarEncuentro(request, id):  # modificacion del encuentro
    # busca en el modelo correspondiente para poder modificar la informacion
    encuentro = get_object_or_404(Encuentro, id=id)
    data = {
        'form': FormularioEncuentro(instance=encuentro)
    }
    if request.method == 'GET':
        formulario = FormularioEncuentro(data=request.GET, instance=encuentro)
        if formulario.is_valid():
            formulario.save()
            print('Se actualizo')
            return redirect(to='/encuentro/')
        data["form"] = formulario
    return render(request, 'editarEncuentros.html', data)


#
#
# Ver 
#
#

def mastorneo(request, id):  # ver torneo
    # busca en el modelo correspondiente para poder ver la informacion
    tor = Torneo.objects.filter(id__icontains=id)
    return render(request, 'masTorneo.html', {"form": tor})


def verEquipo(request, id):  # ver equipo
    # busca en el modelo correspondiente para poder ver la informacion
    equip = Equipo.objects.filter(id__icontains=id)
    return render(request, 'verEquipo.html', {"form": equip})


def verJugador(request, id):  # ver jugador
    # busca en el modelo correspondiente para poder ver la informacion
    jugad = Jugador.objects.filter(id__icontains=id)
    return render(request, 'verJugador.html', {"form": jugad})


def verArbitro(request, id):  # ver arbitro
    # busca en el modelo correspondiente para poder ver la informacion
    arbit = Arbitro.objects.filter(id__icontains=id)
    return render(request, 'verArbitro.html', {"form": arbit})


def verImplemento(request, id):  # ver implemento
    # busca en el modelo correspondiente para poder ver la informacion
    implement = Implementos.objects.filter(id__icontains=id)
    return render(request, 'verImplemento.html', {"form": implement})


def verReserva(request, id):  # ver reserva
    # busca en el modelo correspondiente para poder ver la informacion
    ticket = Ticket.objects.filter(id__icontains=id)
    return render(request, 'verReserva.html', {"form": ticket})


def verEncuentro(request, id):  # ver encuentro
    # busca en el modelo correspondiente para poder ver la informacion
    encuentro = Encuentro.objects.filter(id__icontains=id)
    return render(request, 'verEncuentro.html', {"form": encuentro})


# PERFIL
def perfil(request):  # perfil
    perfil = Persona.objects.all()
    return render(request, 'perfil.html', {"perfil": perfil})


#
#
#
# validacion
#
#
#
def validar(request):
    if request.POST["username"] and request.POST["clave"]:
        usuario = request.POST["username"]
        clave = request.POST["clave"]
        if len(usuario) > 0 and len(clave) > 0:
            personaU = Persona.objects.filter(user__icontains=usuario)
            personaC = Persona.objects.filter(contra__icontains=clave)
            if (personaC and personaU):
                messages.success(request, F"Bienvenido a la administracion")
                return redirect(to="/administrador/")
            else:
                return redirect(to="/loginAdmin/")
        elif len(usuario) == 0 or len(clave) == 0:
            messages.error(request, F"Error cree una cuenta")
            return redirect(to="/loginAdmin/")
    else:
        return redirect(to="/loginAdmin/")
