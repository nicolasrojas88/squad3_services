from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import EmpleadoForm, FormEmpleado, FormCoordinador, CoordinadorForm
from datetime import datetime
from .models import Empleado, Servicio, Coordinador


def alta_empleado_vista(request):
    context = {'form': FormEmpleado()}
    if request.method == "POST":
        post = FormEmpleado()
        post.nombre = request.POST['nombre']
        post.apellido = request.POST['apellido']
        post.numero_legajo = request.POST['numero_legajo']
        graba_datos = Empleado(nombre=post.nombre, apellido=post.apellido, numero_legajo=post.numero_legajo)
        graba_datos.save()

        return render(request, "alta_empleado.html", context)
    else:
        return render(request, "alta_empleado.html", context)


def alta_coordinador_vista(request):
    context = {'form': FormCoordinador()}
    if request.method == "POST":
        post = FormCoordinador()
        post.nombre = request.POST['nombre']
        post.apellido = request.POST['apellido']
        post.numero_documento = request.POST['numero_documento']
        # post.fecha_alta = request.POST['fecha_alta']
        post.fecha_alta = datetime.today().strftime('%Y-%m-%d')
        print(post.fecha_alta)
        graba_datos = Coordinador(nombre=post.nombre, apellido=post.apellido, numero_documento=post.numero_documento,
                                  fecha_alta=post.fecha_alta)
        graba_datos.save()
        return render(request, "alta_coordinador.html", context)
    else:
        return render(request, "alta_coordinador.html", context)


def empleado_activa(request, id_legajo):
    emp = Empleado.objects.get(numero_legajo=id_legajo)
    emp.activo = 1  # set it to whatever you want to update
    emp.save()
    return HttpResponse("se activo,se grabo")


def empleado_desactiva(request, id_legajo):
    emp = Empleado.objects.get(numero_legajo=id_legajo)
    emp.activo = 0  # set it to whatever you want to update
    emp.save()
    return HttpResponse("se DESactivo,se grabo")


def servicio_vista(request, servicio_id):
    servicio = Servicio.objects.filter(id=servicio_id).first()
    return render(request, 'servicio.html', {'servicio': servicio})


def servicios_vista(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios.html', {'servicios': servicios})


def empleados_vista(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados.html', {'empleados': empleados})


def actualizar_empleado_vista(request, empleado_id):
    actualizar_empleado = Empleado.objects.filter(id=empleado_id).first()
    form = EmpleadoForm(instance=actualizar_empleado)
    if request.method == "POST":
        form = EmpleadoForm(request.POST, instance=actualizar_empleado)
        if form.is_valid():
            form.save()
            return redirect('empleados')
    return render(request, 'form_generico.html',{"form": form, "submit_value": "Actualizar Empleado", 'actualizar_empleado': actualizar_empleado, "url_value": 'empleados'})


def coordinadores_vista(request):
    coordinadores = Coordinador.objects.all()
    return render(request, 'coordinadores.html', {'coordinadores': coordinadores})


def actualizar_coordinador_vista(request, coordinador_id):
    actualizar_coordinador = Coordinador.objects.filter(id=coordinador_id).first()
    form = CoordinadorForm(instance=actualizar_coordinador)
    if request.method == "POST":
        form = CoordinadorForm(request.POST, instance=actualizar_coordinador)
        if form.is_valid():
            form.save()
            return redirect('coordinadores')
    return render(request, 'form_generico.html', {"form": form, "submit_value": "Actualizar", 'actualizar_coordinador': actualizar_coordinador, "url_value": 'coordinadores'})

def activar_coordinador(request, coordinador_id):
    estado_coordinador = Coordinador.objects.filter(id=coordinador_id).first()
    if estado_coordinador.activo == False:
        estado_coordinador.activo = True
        estado_coordinador.save()
    return redirect('coordinadores')


def desactivar_coordinador(request, coordinador_id):
    estado_coordinador = Coordinador.objects.filter(id=coordinador_id).first()
    if estado_coordinador.activo == True:
        estado_coordinador.activo = False
        estado_coordinador.save()
    return redirect('coordinadores')
