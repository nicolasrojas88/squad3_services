from django.urls import path
from reservas import views

from reservas import admin

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('alta_emp/', views.alta_empleado_view, name='alta_empleado'),
<<<<<<< HEAD
    path('empleado/activar/<int: id>/', views.empleado_activa, name="empleado_activa"),
=======
    path('servicios', views.servicios_vista, name="servicios"),

>>>>>>> 89208f9b416e2cd8231f180ee10f8e379a8189e3
]
