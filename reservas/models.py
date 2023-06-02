from django.db import models

"""
Nombre del modelo: Empleado.
Los campos son:
nombre: texto
apellido: texto
numero_legajo: entero
activo: boolean (default=True)
"""


class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numero_legajo = models.IntegerField(unique=True)
    activo = models.BooleanField(default=1, blank=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.numero_legajo}  {self.activo} "

class Coordinador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numero_documento = models.IntegerField(unique=True)
    fecha_alta = models.DateField()
    activo = models.BooleanField(default=1, blank=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.numero_documento} {self.fecha_alta} {self.activo} "


class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre}"


class ReservaServicio(models.Model):
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_reserva = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    responsable = models.ForeignKey(Coordinador, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    precio = models.IntegerField()
