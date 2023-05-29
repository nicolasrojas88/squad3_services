from django.contrib import admin

from reservas.models import Empleado, Coordinador, Servicio, Cliente

admin.site.register([Coordinador])
@admin.register(Empleado)
class Empleado(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'numero_legajo', 'activo')
    search_fields=['nombre','apellido']

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'precio', 'activo')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display= ('id', 'nombre', 'apellido', 'activo')
