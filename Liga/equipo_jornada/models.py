from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# from jugador_equipo.models import Equipo
# Create your models here.


class Liga(models.Model):
    nombre = models.CharField(unique=True, max_length=20)
    ciudad = models.CharField(max_length=30)
    anio_creacion = models.IntegerField()
    descripcion = models.CharField(max_length=400, null=True)
    administrador = models.OneToOneField(User)
    fecha_comienzo = models.DateField(null=True)
    contrasena = models.CharField(max_length=20, null=False, default="")
    jornadas_realizadas = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']


class Jornada(models.Model):
    equipo1 = models.ForeignKey(
        'jugador_equipo.Equipo', related_name='primer_equipo+', null=True)
    equipo2 = models.ForeignKey(
        'jugador_equipo.Equipo', related_name='segundo_equipo+', null=True)
    numero = models.IntegerField(null=True)
    fecha = models.DateTimeField(null=True)
    ida = 'ida'
    vuelta = 'vuelta'
    ida_vuelta_choice = (
        (ida, 'ida'),
        (vuelta, 'vuelta'),
    )
    ida_vuelta = models.CharField(
        max_length=10, choices=ida_vuelta_choice, default="ida")
    Liga = models.ForeignKey(Liga, null=True)
    goles_primer_equipo= models.IntegerField(null=True)
    goles_segundo_equipo = models.IntegerField(null =True)

    def __str__(self):
        return self.equipo1.nombre + ' vs ' + self.equipo2.nombre

    class Meta:
        ordering = ['numero']
