# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoffeeFinderApp', '0014_remove_page_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='longitude',
            field=models.DecimalField(default=0.0, max_digits=20, decimal_places=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='latitude',
            field=models.DecimalField(default=0.0, max_digits=20, decimal_places=10),
            preserve_default=True,
        ),
    ]
