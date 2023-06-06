from django.urls import path

from reservas import views

urlpatterns =[
    path('alta_emp/', views.alta_empleado_vista, name='alta_empleado'),
    path('servicios', views.servicios_vista, name="servicios"),
    path("empleado/activar/<id_legajo>/", views.empleado_activa, name="empleado_activa"),
    path("empleado/desactivar/<id_legajo>/", views.empleado_desactiva, name="empleado_activa"),
    path('empleados/listado', views.empleados_vista, name="empleados"),
    path('empleados/modificar/<int:empleado_id>', views.actualizar_empleado_vista, name="actualizar_empleado"),
    path('coordinadores/nuevo/', views.alta_coordinador_vista, name='alta_coordinador'),
    path('coordinadores/listado', views.coordinadores_vista, name="coordinadores"),
    path('coordinadores/modificar/<int:coordinador_id>', views.actualizar_coordinador_vista, name="actualizar_coordinador"),
    path('coordinadores/activar/<int:coordinador_id>', views.activar_coordinador, name="activar_coordinador"),
    path('coordinadores/desactivar/<int:coordinador_id>', views.desactivar_coordinador, name="desactivar_coordinador"),
