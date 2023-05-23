from django.shortcuts import render
from django.shortcuts import render
from .forms import InputForm


# Create your views here.
from .models import Empleado


def alta_empleado_vista(request):
    context = {'form': InputForm()}
    if request.method == "POST":
        post = InputForm()
        post.nombre = request.POST['nombre']
        post.apellido = request.POST['apellido']
        post.numero_legajo = request.POST['numero_legajo']
        graba_datos=Empleado(nombre=post.nombre,apellido=post.apellido,numero_legajo=post.numero_legajo)
        graba_datos.save()

        return render(request, "alta_empleado.html", context)
    else:
        return render(request, "alta_empleado.html", context)

def empleado_activa(request):
