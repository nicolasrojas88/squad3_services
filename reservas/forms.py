from django import forms
from django.forms import ModelForm
from .models import Empleado


class InputForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    numero_legajo = forms.IntegerField()


class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'numero_legajo']
        labels = {'numero_legajo': 'N° de Legajo'}
