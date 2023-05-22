from django.contrib import admin

from reservas.models import Empleado, Coordinador

admin.site.register([Empleado,Coordinador])
