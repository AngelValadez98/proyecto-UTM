from django.db import models

# Create your models here.

class AdministrarEmpleados(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Id Usuario")
    nombre = models.TextField()
    apellidoPa = models.TextField(verbose_name="Apellido Paterno")
    apellidoMa = models.TextField(verbose_name="Apellido Materno")
    area = models.TextField()
    turno = models.TextField()
    imagen = models.ImageField(null=True,upload_to="fotos",verbose_name="Imagen del usuario")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Administrar empleado"
        verbose_name_plural = "Administrar empleados"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre


class ComentarioContacto(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Id Comentario")
    nombre = models.TextField()
    apellidos = models.TextField()
    carreraEspecialidad = models.TextField()
    matricula = models.TextField()
    telefono = models.TextField()
    mensaje = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comentario contacto"
        verbose_name_plural = "Comentarios contactos"
        ordering = ["-created"]

    def __str__(self):
        return self.mensaje

class RegistroSolicitudes(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Id Usuario")
    nombre = models.TextField()
    apellidoPa = models.TextField(verbose_name="Apellido Paterno")
    apellidoMa = models.TextField(verbose_name="Apellido Materno")
    carreraEspecialidad = models.TextField()
    matricula = models.TextField()
    telefono = models.TextField()
    turno = models.TextField()
    correoElectronico = models.EmailField()
    material = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Registro de solicitud"
        verbose_name_plural = "Registro de solicitudes"
        ordering = ["-created"]

    def __str__(self):
        return self.carreraEspecialidad