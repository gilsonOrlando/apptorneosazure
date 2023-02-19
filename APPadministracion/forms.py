import re
from django import forms
from APPadministracion.models import Persona, Torneo, Arbitro, Ticket, Equipo, Jugador, Implementos, Encuentro

from django.core.exceptions import ValidationError


def validate_password_strength(value):
    min_length = 8
    print("Se ingreso a la funcion de comprobar contraselas")
    if len(value) < min_length:
        print("La contrasela es muy corta")
        raise ValidationError(f"La contraseña debe tener al menos {min_length} caracteres.")

    if not any(char.isdigit() for char in value):
        print("La contrasela no tiene numeros")
        raise ValidationError("La contraseña debe incluir al menos un número.")

    if not any(char.isupper() for char in value):
        print("La contrasela no tiene mayusculas")
        raise ValidationError("La contraseña debe incluir al menos una letra mayúscula.")

    if not any(char.islower() for char in value):
        print("La contrasela no tiene minusculas")
        raise ValidationError("La contraseña debe incluir al menos una letra minúscula.")

    if not any(char in ['$', '@', '#', '%'] for char in value):
        print("La contrasela no tiene caracteres especiales")
        raise ValidationError("La contraseña debe incluir al menos un carácter especial: $ @ # %")


def validate_cellphone(cellphone):
    if not re.match(r'^\+?1?\d{9,15}$', cellphone):
        print("El numero de celular no es valido")
        raise ValidationError("Número de teléfono no válido")


def validate_cedula(cedula):
    if not re.match(r'^\+?1?\d{9,15}$', cedula):
        print("El numero de cedula no es valido")
        raise ValidationError("Número de cedula no válido")


def clean_nombre(nombre):
    if not nombre.isalpha():
        raise ValidationError('El nombre no puede contener números')


# creamos los formularios para cada una de las clases
class FormularioPersona(forms.ModelForm):
    contra = forms.CharField(widget=forms.PasswordInput, validators=[validate_password_strength])
    celular = forms.CharField(validators=[validate_cellphone])
    cedula = forms.CharField(validators=[validate_cedula])
    nombre = forms.CharField(validators=[clean_nombre])

    class Meta:
        model = Persona
        fields = ["nombre", "apellido", "correo", "celular", "cedula", "user", "contra"]
        widgets = {
            'contra': forms.PasswordInput(),
            'correo': forms.EmailInput(),
            'telefono': forms.TextInput(),
            'cedula': forms.TextInput(),
            'user': forms.TextInput(),
        }
        required = {
            'contra': True,
            'correo': True,
            'user': True,
            'cedula': True,
            'celular': True,
            'apellido': True,
            'nombre': True,
        }
        min_length = {
            'contra': 8,
            'telefono': 10,
            'cedula': 10,
        }
        max_length = {
            'contra': 16,
        }
        labels = {
            'contra': 'Contraseña',
            'correo': 'Correo',
            'user': 'Usuario',
            'cedula': 'Cedula',
        }

        help_texts = {
            'contra': 'La contraseña debe tener al menos 8 caracteres, al menos un número, al menos una letra mayúscula y al menos un carácter especial $, #, @, %.',
        }


class FormularioTorneo(forms.ModelForm):
    class Meta:
        model = Torneo
        fields = ["nombre", "alias", "numeroEquipo", "descripcion", "fechaInicio", "fechaFin", "tipo_Tor"]


class FormularioArbitro(forms.ModelForm):
    class Meta:
        model = Arbitro
        fields = ["PropiedadTorneo", "nombre", "apellido", "correo", "celular", "cedula"]


class FormularioImplementos(forms.ModelForm):
    class Meta:
        model = Implementos
        fields = ["PropiedadTorneo", "nombre", "cantidad", "descripcion", "tipo_Im"]


class FormularioTicket(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["PropiedadTorneo", "nombre", "apellido", "correo", "cedula", "estado_Ticket"]


class FormularioEquipo(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ["PropiedadTorneo", "nombre", "alias", "frase", "entrenador", "cantidadJugador", "estado_Equipo"]


class FormularioJugador(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ["PropiedadEquipo", "nombre", "apellido", "correo", "celular", "cedula", "posicion_Jugador"]


class FormularioEncuentro(forms.ModelForm):
    class Meta:
        model = Encuentro
        fields = ["PropiedadTorneo", "nombreA", "nombreB", "fechaPartido", "hora", "golesA", "golesB", "faltas",
                  "tarjetaRoja", "tarjetaAmarilla"]
