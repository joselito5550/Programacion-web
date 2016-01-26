# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipo_jornada', '0002_auto_20160125_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='jornada',
            name='fecha',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='jornada',
            name='ida_vuelta',
            field=models.CharField(default=b'ida', max_length=10),
        ),
    ]
