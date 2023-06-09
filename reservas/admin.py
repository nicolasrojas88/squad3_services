from django.contrib import admin

from reservas.models import Empleado, Coordinador, Servicio, Cliente, Reserva, Servicio

# admin.site.register([Coordinador])
# admin.site.register([Reserva])


@admin.register(Empleado)
class Empleado(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'numero_legajo', 'activo')
    search_fields = ['nombre', 'apellido']


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'precio', 'activo')


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'activo')


@admin.register(Coordinador)
class Coordinador(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'numero_documento', 'fecha_alta', 'activo')
    search_fields = ['nombre', 'apellido']


@admin.register(Reserva)
class Reserva(admin.ModelAdmin):
    list_display = ('fecha_creacion', 'fecha_reserva', 'cliente', 'coordinador', 'empleado', 'servicio', 'precio')
    search_fields = []
