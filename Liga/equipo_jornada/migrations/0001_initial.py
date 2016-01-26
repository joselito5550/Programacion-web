# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Jornada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField(null=True)),
            ],
            options={
                'ordering': ['numero'],
            },
        ),
        migrations.CreateModel(
            name='Liga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=20)),
                ('ciudad', models.CharField(max_length=30)),
                ('anio_creacion', models.IntegerField()),
                ('descripcion', models.CharField(max_length=400, null=True)),
                ('fecha_comienzo', models.DateField(null=True)),
                ('jornadas_realizadas', models.BooleanField(default=False)),
                ('administrador', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
    ]
