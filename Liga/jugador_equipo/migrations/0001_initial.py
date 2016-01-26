# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('equipo_jornada', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=20)),
                ('ciudad', models.CharField(max_length=30)),
                ('anio_creacion', models.IntegerField(default=0)),
                ('descripcion', models.CharField(max_length=400, null=True)),
                ('nombre_del_entrenador', models.CharField(max_length=20)),
                ('puntos', models.IntegerField(default=0)),
                ('Liga', models.ForeignKey(blank=True, to='equipo_jornada.Liga', null=True)),
                ('administrador', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Perfiles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telefono', models.IntegerField()),
                ('equipo', models.ForeignKey(blank=True, to='jugador_equipo.Equipo', null=True)),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
