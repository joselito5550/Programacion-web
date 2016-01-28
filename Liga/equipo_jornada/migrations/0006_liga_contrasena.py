# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipo_jornada', '0005_jornada_liga'),
    ]

    operations = [
        migrations.AddField(
            model_name='liga',
            name='contrasena',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
