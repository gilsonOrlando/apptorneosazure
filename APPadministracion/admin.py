from django.contrib import admin
from APPadministracion.models import Persona, Torneo, Arbitro, Ticket, Equipo, Jugador, Implementos, Encuentro
# Register your models here.
#registro del modelo persona
class AdminPersona(admin.ModelAdmin):
    list_display = ["__str__","nombre","apellido","correo","celular","cedula","user","contra"]
    search_fields=("nombre","cedula","apellido")
    filter = ("apellido") #nos permite filtrar informacion por apellidos 
    class Meta(object):
        model = Persona
admin.site.register(Persona,AdminPersona)


#registro del modelo arbitro
class AdminArbitro(admin.ModelAdmin):
    list_display = ["__str__","nombre","apellido","correo","celular","cedula","PropiedadTorneo"]
    search_fields=("nombre","cedula", "apellido")
    filter = ("apellido") #nos permite filtrar informacion por apellidos 
    class Meta(object):
        model = Arbitro
admin.site.register(Arbitro,AdminArbitro)

#registro del modelo jugador
class AdminJugador(admin.ModelAdmin):
    list_display = ["__str__","nombre","apellido","correo","celular","cedula","posicion_Jugador","PropiedadEquipo"]
    search_fields=("nombre","cedula", "apellido")
    filter = ("apellido") #nos permite filtrar informacion por apellidos 
    class Meta(object):
        model = Jugador
admin.site.register(Jugador,AdminJugador)

#registro del modelo torneo
class AdminTorneo(admin.ModelAdmin):
    list_display = ["__str__","nombre","alias","numeroEquipo","descripcion","fechaInicio","fechaFin","tipo_Tor"]
    search_fields=("nombre","alias")
    filter = ("nombre") #nos permite filtrar informacion por apellidos 
    class Meta(object):
        model = Torneo
admin.site.register(Torneo,AdminTorneo)

#registro del modelo implemento
class AdminImplemento(admin.ModelAdmin):
    list_display = ["__str__","nombre","cantidad","descripcion","tipo_Im","PropiedadTorneo"]
    search_fields=("nombre","descripcion")
    filter = ("nombre") #nos permite filtrar informacion por apellidos 
    class Meta(object):
        model = Implementos
admin.site.register(Implementos,AdminImplemento)

#registro del modelo ticket
class AdminTicket(admin.ModelAdmin):
    list_display = ["__str__","nombre","apellido","correo","cedula","estado_Ticket","PropiedadTorneo"]
    search_fields=("nombre","apellido")
    filter = ("nombre") #nos permite filtrar informacion por apellidos 
    class Meta(object):
        model = Ticket
admin.site.register(Ticket,AdminTicket)

#registro del modelo ticket
class AdminEquipo(admin.ModelAdmin):
    list_display = ["__str__","nombre","alias","frase","entrenador","cantidadJugador","estado_Equipo","PropiedadTorneo"]
    search_fields=("nombre","alias")
    filter = ("nombre") #nos permite filtrar informacion por apellidos 
    class Meta(object):
        model = Equipo
admin.site.register(Equipo,AdminEquipo)

#registro del modelo encuentro
class AdminEncuentro(admin.ModelAdmin):
    list_display = ["__str__","nombreA","nombreB","fechaPartido","golesA","golesB","faltas","tarjetaRoja","tarjetaAmarilla","PropiedadTorneo"]
    search_fields=("nombreA","nombreB")
    filter = ("nombreA") #nos permite filtrar informacion por nombre de equipo de encuentro 
    class Meta(object):
        model = Encuentro
admin.site.register(Encuentro,AdminEncuentro)