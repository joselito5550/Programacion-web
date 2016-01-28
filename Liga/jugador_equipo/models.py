from django.db import models
from django.contrib.auth.models import User
from equipo_jornada.models import Liga, Jornada

# Create your models here.


class Equipo(models.Model):
    nombre = models.CharField(unique=True, max_length=20)
    ciudad = models.CharField(max_length=30)
    anio_creacion = models.IntegerField(default=0)
    descripcion = models.CharField(max_length=400, null=True)
    nombre_del_entrenador = models.CharField(max_length=20)
    puntos = models.IntegerField(default=0)
    administrador = models.OneToOneField(User)
    Liga = models.ForeignKey(Liga, null=True, blank=True)
    contrasena = models.CharField(max_length=20, null=False, default="")


    def __str__(self):
        return self.nombre  

    class Meta:
        ordering = ['nombre']


class Perfiles(models.Model):
    usuario = models.OneToOneField(User)
    telefono = models.IntegerField()
    equipo = models.ForeignKey(Equipo, null=True, blank=True)

    def __unicode__(self):
        return self.usuario.username
