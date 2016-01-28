# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jugador_equipo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='contrasena',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
