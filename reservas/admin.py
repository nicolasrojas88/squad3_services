from django.contrib import admin

from reservas.models import Empleado, Coordinador, Servicio

#admin.site.register([Empleado,Coordinador])


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'precio', 'activo')
