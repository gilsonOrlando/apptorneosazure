from django.db import models


# Create your models here.

# Clase que hara referencia al perfil de usuario
class Persona(models.Model):
    nombre = models.CharField(max_length=140, blank=False, null=True)
    apellido = models.CharField(max_length=140, blank=False, null=True)
    correo = models.EmailField(unique=True, blank=True, null=True)
    celular = models.CharField(max_length=10, blank=False, null=True)
    cedula = models.CharField(max_length=10, blank=False, unique=True, null=True)
    user = models.CharField(max_length=15, blank=False, null=True, unique=True)
    contra = models.CharField(max_length=15, blank=False, null=True)


# Clase que tendra los datos de cada torneo
class Torneo(models.Model):
    tipoTorneo = (('eliminatoria', 'eliminatoria'), ('corriente', 'corriente'),)
    nombre = models.CharField(max_length=30, blank=False)
    alias = models.CharField(max_length=30, blank=False)
    numeroEquipo = models.CharField(max_length=3, blank=False)
    descripcion = models.CharField(max_length=50, blank=False)
    fechaInicio = models.CharField(max_length=10, blank=False)
    fechaFin = models.CharField(max_length=10, blank=False)
    tipo_Tor = models.CharField(max_length=30, choices=tipoTorneo, default="", blank=False)


# Clase que maneja los datos de los arbitros que se permiten registrar por torneo
class Arbitro(models.Model):
    PropiedadTorneo = models.ForeignKey(Torneo, on_delete=models.CASCADE, default="")
    nombre = models.CharField(max_length=30, blank=False)
    apellido = models.CharField(max_length=30, blank=False)
    correo = models.EmailField()
    celular = models.CharField(max_length=10, blank=False)
    cedula = models.CharField(max_length=10, blank=False)


# Clase que maneja los implementos deportivos que se usan por cada torneo
class Implementos(models.Model):
    tipoimplemento = (('donado', 'donado'), ('comprado', 'comprado'),)
    PropiedadTorneo = models.ForeignKey(Torneo, on_delete=models.CASCADE, default="")
    nombre = models.CharField(max_length=30, blank=False)
    cantidad = models.IntegerField()
    descripcion = models.TextField(max_length=50, blank=False)
    tipo_Im = models.CharField(max_length=30, choices=tipoimplemento, default="", blank=False)


# Clase que permite controlar las reservaciones de las entradas
class Ticket(models.Model):
    PropiedadTorneo = models.ForeignKey(Torneo, on_delete=models.CASCADE, default="")
    nombre = models.CharField(max_length=30, blank=False)
    apellido = models.CharField(max_length=30, blank=False)
    correo = models.EmailField()
    cedula = models.CharField(max_length=10, blank=False)
    estado = (('espera', 'espera'), ('comprado', 'comprado'),)
    estado_Ticket = models.CharField(max_length=30, choices=estado, default="", blank=False)


# Clase para ingresar el equipo que participa en los torneos
class Equipo(models.Model):
    estado = (('activo', 'activo'), ('eliminado', 'eliminado'),)
    PropiedadTorneo = models.ForeignKey(Torneo, on_delete=models.CASCADE, default="")
    nombre = models.CharField(max_length=30, blank=False)
    alias = models.CharField(max_length=30, blank=False)
    frase = models.CharField(max_length=30, blank=False)
    entrenador = models.CharField(max_length=30, blank=False)
    cantidadJugador = models.IntegerField()
    estado_Equipo = models.CharField(max_length=30, choices=estado, default="", blank=False)


# Clase para la informacion de los jugadores de cada equipo
class Jugador(models.Model):
    posicion = (
    ('mediocampista', 'mediocampista'), ('defensa', 'defensa'), ('portero', 'portero'), ('delantero', 'delantero'),)
    PropiedadEquipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, default="")
    nombre = models.CharField(max_length=30, blank=False)
    apellido = models.CharField(max_length=30, blank=False)
    correo = models.EmailField()
    celular = models.CharField(max_length=10, blank=False)
    cedula = models.CharField(max_length=10, blank=False)
    posicion_Jugador = models.CharField(max_length=30, choices=posicion, default="", blank=False)


# Clase para la informacion de los encuentros de cada torneo
class Encuentro(models.Model):
    PropiedadTorneo = models.ForeignKey(Torneo, on_delete=models.CASCADE, default="")
    nombreA = models.CharField(max_length=30, blank=False)
    nombreB = models.CharField(max_length=30, blank=False)
    fechaPartido = models.DateField("(ddd/mmm/yyy)", auto_now_add=False, auto_now=False, blank=False)
    hora = models.CharField(max_length=10, blank=False)
    golesA = models.IntegerField(default=0, blank=False)
    golesB = models.IntegerField(default=0, blank=False)
    faltas = models.IntegerField(default=0, blank=False)
    tarjetaRoja = models.IntegerField(default=0, blank=False)
    tarjetaAmarilla = models.IntegerField(default=0, blank=False)
