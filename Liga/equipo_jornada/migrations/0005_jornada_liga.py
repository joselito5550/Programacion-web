# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipo_jornada', '0004_auto_20160126_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='jornada',
            name='Liga',
            field=models.ForeignKey(to='equipo_jornada.Liga', null=True),
        ),
    ]
