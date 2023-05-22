from django import forms


# creating a form
class InputForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    numero_legajo = forms.IntegerField()



