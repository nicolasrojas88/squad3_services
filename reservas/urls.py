from django.urls import path

from reservas import views

urlpatterns =[
    path('servicios/nuevo', views.alta_servicio_vista, name='alta_servicio'),
    path('servicios/listado', views.servicios_vista, name="servicios"),
    path('servicios/modificar/<int:servicio_id>', views.actualizar_servicio_vista, name="actualizar_servicio"),
    path('servicios/activar/<int:servicio_id>', views.activar_servicio, name="activar_servicio"),
    path('servicios/desactivar/<int:servicio_id>', views.desactivar_servicio, name="desactivar_servicio"),

    path('empleados/nuevo', views.alta_empleado_vista, name='alta_empleado'),
    path('empleados/listado', views.empleados_vista, name="empleados"),
    path('empleados/modificar/<id_legajo>', views.actualizar_empleado_vista, name="actualizar_empleado"),
    path("empleados/activar/<id_legajo>/", views.empleado_activa, name="empleado_activa"),
    path("empleados/desactivar/<id_legajo>/", views.empleado_desactiva, name="empleado_desactiva"),

    path('coordinadores/nuevo/', views.alta_coordinador_vista, name='alta_coordinador'),
    path('coordinadores/listado', views.coordinadores_vista, name="coordinadores"),
    path('coordinadores/modificar/<int:coordinador_id>', views.actualizar_coordinador_vista, name="actualizar_coordinador"),
    path('coordinadores/activar/<int:coordinador_id>', views.activar_coordinador, name="activar_coordinador"),
    path('coordinadores/desactivar/<int:coordinador_id>', views.desactivar_coordinador, name="desactivar_coordinador"),

    path('clientes/nuevo/', views.alta_cliente_vista, name='alta_cliente'),
    path('clientes/listado', views.clientes_vista, name="clientes"),
    path('clientes/modificar/<int:cliente_id>', views.actualizar_cliente_vista, name="actualizar_cliente"),
    path('clientes/activar/<int:cliente_id>', views.activar_cliente, name="activar_cliente"),
    path('clientes/desactivar/<int:cliente_id>', views.desactivar_cliente, name="desactivar_cliente"),

    path('reservas/nuevo/', views.alta_reserva_vista, name='alta_reserva'),
    path('reservas/listado', views.reservas_vista, name="reservas"),
    path('reservas/modificar/<int:reserva_id>', views.actualizar_reserva_vista, name="actualizar_reserva"),
    path('reservas/eliminar/<int:reserva_id>', views.actualizar_reserva_vista, name="actualizar_reserva"),

]