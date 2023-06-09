from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import EmpleadoForm, FormEmpleado, FormCoordinador, CoordinadorForm, ClienteForm, ServicioForm, ReservaForm
from datetime import datetime
from .models import Empleado, Servicio, Coordinador, Reserva, Cliente


def alta_empleado_vista(request):
    context = {'form': FormEmpleado()}
    if request.method == "POST":
        post = FormEmpleado()
        post.nombre = request.POST['nombre']
        post.apellido = request.POST['apellido']
        post.numero_legajo = request.POST['numero_legajo']
        graba_datos = Empleado(nombre=post.nombre, apellido=post.apellido, numero_legajo=post.numero_legajo)
        graba_datos.save()

        #return render(request, "alta_empleado.html", context)
        return redirect('empleados')
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
        #return render(request, "tabla_coordinador.html", context)
        return redirect('coordinadores')
    else:
        return render(request, "alta_coordinador.html", context)


def empleado_activa(request, id_legajo):
    estado_empleado = Empleado.objects.filter(id=id_legajo).first()
    if estado_empleado.activo == False:
        estado_empleado.activo = True
        estado_empleado.save()
    return redirect('empleados')


def empleado_desactiva(request, id_legajo):
    estado_empleado = Empleado.objects.filter(id=id_legajo).first()
    if estado_empleado.activo == True:
        estado_empleado.activo = False
        estado_empleado.save()
    return redirect('empleados')


def servicio_vista(request, servicio_id):
    servicio = Servicio.objects.filter(id=servicio_id).first()
    return render(request, 'servicio.html', {'servicio': servicio})


def alta_servicio_vista(request):
    form = ServicioForm()
    if request.method == "POST":
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicios')
    return render(request, 'form_generico.html', {"form": form, "submit_value": "Enviar", "url_value": 'servicios'})


def servicios_vista(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios.html', {'servicios': servicios})


def actualizar_servicio_vista(request, servicio_id):
    actualizar_servicio = Servicio.objects.filter(id=servicio_id).first()
    form = ServicioForm(instance=actualizar_servicio)
    if request.method == "POST":
        form = ServicioForm(request.POST, instance=actualizar_servicio)
        if form.is_valid():
            form.save()
            return redirect('servicios')
    return render(request, 'form_generico.html', {"form": form, "submit_value": "Actualizar", 'actualizar_servicio': actualizar_servicio, "url_value": 'reservas'})


def activar_servicio(request, servicio_id):
    estado_servicio = Servicio.objects.filter(id=servicio_id).first()
    if estado_servicio.activo == False:
        estado_servicio.activo = True
        estado_servicio.save()
    return redirect('servicios')


def desactivar_servicio(request, servicio_id):
    estado_servicio = Coordinador.objects.filter(id=servicio_id).first()
    if estado_servicio.activo == True:
        estado_servicio.activo = False
        estado_servicio.save()
    return redirect('servicios')


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
    return render(request, 'form_generico.html',{"form": form, "submit_value": "Actualizar", 'actualizar_empleado': actualizar_empleado, "url_value": 'empleados'})


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


def alta_reserva_vista(request):
    form = ReservaForm()
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservas')
    return render(request, 'form_reserva.html', {"form": form, "submit_value": "Enviar", "url_value": 'reservas'})


def reservas_vista(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas.html', {'reservas': reservas})


def actualizar_reserva_vista(request, reserva_id):
    actualizar_reserva = Reserva.objects.filter(id=reserva_id).first()
    form = ReservaForm(instance=actualizar_reserva)
    if request.method == "POST":
        form = ReservaForm(request.POST, instance=actualizar_reserva)
        if form.is_valid():
            form.save()
            return redirect('reservas')
    return render(request, 'form_reserva.html', {"form": form, "submit_value": "Actualizar", 'actualizar_reserva': actualizar_reserva, "url_value": 'reservas'})


def eliminar_reserva(request, reserva_id):
    reserva = Reserva.objects.filter(id=reserva_id).first()
    reserva.delete()
    return redirect('reservas')

#########################################################################


def alta_cliente_vista(request):
    form = ClienteForm()
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    return render(request, 'form_generico.html', {"form": form, "submit_value": "Enviar", "url_value": 'clientes'})


def clientes_vista(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})


def actualizar_cliente_vista(request, cliente_id):
    actualizar_cliente = Cliente.objects.filter(id=cliente_id).first()
    form = ClienteForm(instance=actualizar_cliente)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=actualizar_cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    return render(request, 'form_generico.html', {"form": form, "submit_value": "Actualizar", 'actualizar_cliente': actualizar_cliente, "url_value": 'clientes'})


def activar_cliente(request, cliente_id):
    estado_cliente = Cliente.objects.filter(id=cliente_id).first()
    if estado_cliente.activo == False:
        estado_cliente.activo = True
        estado_cliente.save()
    return redirect('clientes')


def desactivar_cliente(request, cliente_id):
    estado_cliente = Cliente.objects.filter(id=cliente_id).first()
    if estado_cliente.activo == True:
        estado_cliente.activo = False
        estado_cliente.save()
    return redirect('clientes')
