# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipo_jornada', '0003_auto_20160126_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jornada',
            name='ida_vuelta',
            field=models.CharField(default=b'ida', max_length=10, choices=[(b'ida', b'ida'), (b'vuelta', b'vuelta')]),
        ),
    ]
