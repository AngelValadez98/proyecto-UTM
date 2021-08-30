from django import forms
from .models import ComentarioContacto
from .models import RegistroSolicitudes

class ComentarioContactoForm(forms.ModelForm):
    class Meta:
        model = ComentarioContacto
        fields = ['nombre','apellidos','carreraEspecialidad','matricula','telefono','mensaje']

class RegistroSolicitudesForm(forms.ModelForm):
    class Meta:
        model = RegistroSolicitudes
        fields = ['nombre','apellidoPa','apellidoMa','carreraEspecialidad','matricula','telefono','turno','correoElectronico','material']