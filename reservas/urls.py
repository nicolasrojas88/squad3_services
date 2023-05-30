from django.urls import path

from reservas import views

urlpatterns =[
    path('alta_emp/', views.alta_empleado_vista, name='alta_empleado'),
    path('servicios', views.servicios_vista, name="servicios"),
    path("empleado/activar/<int:id_legajo>/", views.empleado_activa, name="empleado_activa"),
    path("empleado/desactivar/<int:id_legajo>/", views.empleado_desactiva, name="empleado_activa")
]