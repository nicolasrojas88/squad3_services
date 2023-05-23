from django.urls import path
from reservas import views

from reservas import admin

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('alta_emp/', views.alta_empleado_view, name='alta_empleado'),
    path('empleado/activar/<int: id>/', views.empleado_activa, name="empleado_activa"),
]
