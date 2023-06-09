from django import forms
from django.forms import ModelForm, widgets
from .models import Empleado, Coordinador, Servicio, Cliente, Reserva


class FormEmpleado(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    numero_legajo = forms.IntegerField()


class FormCoordinador(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    numero_documento = forms.IntegerField()
    fecha_alta = forms.DateField()


class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'numero_legajo']
        labels = {'numero_legajo': 'N° de Legajo'}


class CoordinadorForm(ModelForm):
    class Meta:
        model = Coordinador
        fields = ['nombre', 'apellido', 'numero_documento']
        labels = {'numero_documento': 'Numero de DNI'}


class ServicioForm(ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'precio']
        labels = {}


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido']
        labels = {}


class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        fields = ['fecha_reserva', 'cliente', 'servicio', 'precio', 'empleado', 'coordinador']
        labels = {'fecha_reserva': 'Fecha de Reserva'}
        widgets = {
            'fecha_reserva': widgets.DateInput(attrs={'type': 'date'})
        }