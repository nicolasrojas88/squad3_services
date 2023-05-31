from django.http import HttpResponse
from django.shortcuts import render
from .forms import InputForm

# Create your views here.
from .models import Empleado, Servicio


def alta_empleado_vista(request):
    context = {'form': InputForm()}
    if request.method == "POST":
        post = InputForm()
        post.nombre = request.POST['nombre']
        post.apellido = request.POST['apellido']
        post.numero_legajo = request.POST['numero_legajo']
        graba_datos = Empleado(nombre=post.nombre, apellido=post.apellido, numero_legajo=post.numero_legajo)
        graba_datos.save()


        return render(request, "alta_empleado.html", context)
    else:
        return render(request, "alta_empleado.html", context)


def empleado_activa(request, id_legajo):

    emp = Empleado.objects.get(numero_legajo=id_legajo)
    emp.activo = 1  # set it to whatever you want to update
    emp.save()
    return HttpResponse ("se activo,se grabo" )

def empleado_desactiva(request, id_legajo):

    emp = Empleado.objects.get(numero_legajo=id_legajo)
    emp.activo = 0  # set it to whatever you want to update
    emp.save()
    return HttpResponse ("se DESactivo,se grabo" )

def servicio_vista(request, servicio_id):
    servicio = Servicio.objects.filter(id=servicio_id).first()
    return render(request, 'servicio.html', {'servicio': servicio})


def servicios_vista(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios.html', {'servicios': servicios})

def actualizar_empleado_vista(request, empleado_id):
    actualizar_empleado = Empleado.objects.filter(id=empleado_id).first()
    form = EmpleadoForm(instance=actualizar_empleado)
    if request.method == "POST":
        form = EmpleadoForm(request.POST, instance=actualizar_empleado)
        if form.is_valid():
            form.save()
            return redirect('empleados')

    return render(request, 'form_generico.html', {"form": form, "submit_value": "Actualizar Empleado", 'actualizar_empleado': actualizar_empleado})
