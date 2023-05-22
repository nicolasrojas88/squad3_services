from django.shortcuts import render
from .forms import InputForm


# Create your views here.
from .models import Empleado,Servicio


def alta_empleado_view(request):
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


def servicio_vista(request, servicio_id):
    servicio = Servicio.objects.filter(id=servicio_id).first()
    return render(request, 'servicio.html', {'servicio': servicio})


def servicios_vista(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios.html', {'servicios': servicios})
