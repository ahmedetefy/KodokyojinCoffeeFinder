# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0042_auto_20150320_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='latitude',
            field=models.DecimalField(default=0.0, max_digits=50, decimal_places=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='longitude',
            field=models.DecimalField(default=0.0, max_digits=50, decimal_places=30),
            preserve_default=True,
        ),
    ]
