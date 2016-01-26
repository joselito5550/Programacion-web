# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipo_jornada', '0001_initial'),
        ('jugador_equipo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jornada',
            name='equipo1',
            field=models.ForeignKey(related_name='primer_equipo+', to='jugador_equipo.Equipo', null=True),
        ),
        migrations.AddField(
            model_name='jornada',
            name='equipo2',
            field=models.ForeignKey(related_name='segundo_equipo+', to='jugador_equipo.Equipo', null=True),
        ),
    ]
