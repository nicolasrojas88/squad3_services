from django.urls import path
from reservas import views

from reservas import admin

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('alta_emp/', views.alta_empleado_view, name='alta_empleado'),

]
