# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipo_jornada', '0006_liga_contrasena'),
    ]

    operations = [
        migrations.AddField(
            model_name='jornada',
            name='goles_primer_equipo',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='jornada',
            name='goles_segundo_equipo',
            field=models.IntegerField(null=True),
        ),
    ]
