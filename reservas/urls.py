from django.urls import path

from reservas import views

urlpatterns =[
    path('alta_emp/', views.alta_empleado_vista, name='alta_empleado'),
    path('servicios', views.servicios_vista, name="servicios"),
    path("empleado/activar/<id_legajo>/", views.empleado_activa, name="empleado_activa"),
    path("empleado/desactivar/<id_legajo>/", views.empleado_desactiva, name="empleado_activa"),
    path('empleados/<int:empleado_id>', views.actualizar_empleado_vista, name="actualizar_empleado"),
]